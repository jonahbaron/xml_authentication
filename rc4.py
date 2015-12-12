#!/usr/bin/env python

import string
import argparse

def ksa(key):
	klen = len(key)

	string = range(256)

	j = 0
	for i in range(256):
		j = (j + string[i] + key[i % klen]) % 256
		temp = string[i]
		string[i] = string[j]
		string[j] = temp
	print string, key

	return string

def rc4(pstring,key):
	key = [ord(char) for char in key]
	string = [ord(char) for char in pstring]
	tempstring = ksa(key)

	print key

	cstring = pstring

	return cstring

def rc4file(fname):
	with open(fname) as f:
		fcontent = f.readlines()

	newcontent = []
	for s in fcontent:
		s = s.strip()
		rc4line = rc4(s)
		#print rc4line
		newcontent.append(rc4line)

	with open("output.txt", "w") as f:
		for s in newcontent:
			f.write(s + "\n")

def main():
	parser = argparse.ArgumentParser(description="Encrypt or decrypt with RC4")
	parser.add_argument("key", type=str, help="key/password to encrypt or decrypt")
	parser.add_argument("-s", "--string", type=str, help="encrypt or decrypt an entered string")
	parser.add_argument("-f", "--filename", type=str, help="encrypt or decrypt an entered file and write output to output.txt")
	args = parser.parse_args()

	key = args.key
	string = args.string
	fname = args.filename

	if args.filename is not None:
		rc4file(fname)

	elif args.string is not None:
		output = rc4(string,key)
		print output
	else:
		print "RC4 Encryptor/Decryptor"
		print "Please run './rc4.py -h'"

if __name__ == "__main__":
	main()
