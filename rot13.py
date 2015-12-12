#!/usr/bin/env python

import string
import argparse

def rot13(text1):
	rot = string.maketrans(
		"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
		"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

	text2 = string.translate(text1, rot)

	return text2

def rot13file(fname):
	with open(fname) as f:
		fcontent = f.readlines()

	newcontent = []
	for s in fcontent:
		s = s.strip()
		rot13line = rot13(s)
		#print rot13line
		newcontent.append(rot13line)

	with open("output.txt", "w") as f:
		for s in newcontent:
			f.write(s + "\n")

def main():
	parser = argparse.ArgumentParser(description="Encrypt or decrypt a string")
	parser.add_argument("-s", "--string", type=str, help="encrypt or decrypt an entered string (ROT13 encryption = ROT13 decryption)")
	parser.add_argument("-f", "--filename", type=str, help="encrypt or decrypt an entered file and write output to output.txt")
	args = parser.parse_args()

	string = args.string
	fname = args.filename
	

	if args.filename is not None:
		rot13file(fname)
		
	elif args.string is not None:
		output = rot13(args.string)
		print output
	else:
		print "ROT13 Encryptor/Decryptor"
		print "Please run './rot13.py -h'"

if __name__ == "__main__":
	main()
