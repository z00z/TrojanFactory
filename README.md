# TrojanFactory

Simple python script to generate trojans.

The Trojan Factory is designed to be as generic as possible, it can be used to embed evil files within any normal file, it does this using an Autoit download-and-execute script, so basically it takes 2 urls:
1. One for a normal file (can be a pdf, mp3. doc, exe ...etc);
2. And an evil file (backdoor, keylogger ...etc).
The result is one exe that when executed, it presents the normal file (file 1) to the user and runs the evil file in the background.

Features:
- Can be used with any file type (pdf, mp3. png, jpg ...etc).
- Works with updated systems because it does NOT rely on a vulnerability, its simply a download and execute script.
- Automatically sets the right icon depending on file 1.
- User can also use a custom icon.
- Trojan can be packaged into a zip automatically using the --zip argument.

Requirements:
  - Autoit (https://www.autoitscript.com/site/autoit/downloads/).
  
Installation:
  1. Download AutoIt (https://www.autoitscript.com/site/autoit/downloads/).
  2. Install it using wine
    > wine autoit-v3-setup.exe
  3. Clone Trojan Factory:
    > git clone https://github.com/z00z/TrojanFactory.git
  4. You're all set, navigare into TrojanFactory
    > cd TrojanFactory
  5. Run --help for usage
    > python trojan_factory.py --help
