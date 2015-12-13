#!/usr/bin/env python

import base64
import argparse

def rc4(string,key):
	string = [ord(char) for char in string]
	key = [ord(char) for char in key]

	klen = len(key)
	S = range(256)

	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % klen]) % 256
		S[i], S[j] = S[j], S[i]

	i = 0
	j = 0
	newchars = []
	for char in string:
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]
		newchars.append(char ^ S[(S[i] + S[j]) % 256])

	newchars = [chr(char) for char in newchars]
	newstring = ''.join(newchars)

	return newstring

def encfile(fname,key,outfile):
	with open(fname) as f:
		fcontent = f.readlines()
	#print fcontent

	encoding = base64.b64encode
	output = []

	for pstring in fcontent:
		pstring = pstring.strip()
		pstring = rc4(pstring,key)
		cstring = encoding(pstring)
		#print cstring
		output.append(cstring + '\n')
	#print output

	with open(outfile, "wb") as f:
		for line in output:
			f.write(line)

def decfile(fname,key,outfile):
	with open(fname) as f:
		fcontent = f.readlines()
	#print fcontent

	decoding = base64.b64decode
	output = []

	for cstring in fcontent:
		cstring = cstring.strip()
		cstring = decoding(cstring)
		pstring = rc4(cstring,key)
		#print pstring
		output.append(pstring + '\n')
	#print output

	with open(outfile, "wb") as f:
		for line in output:
			f.write(line)

def main():
	parser = argparse.ArgumentParser(description="Encrypt or decrypt a file with RC4")
	#parser.add_argument("filename", type=str, help="file to encrypt or decrypt")
	parser.add_argument("key", type=str, help="key/password to encrypt or decrypt")
	parser.add_argument("-e", "--encrypt", type=str, help="file to encrypt")
	parser.add_argument("-d", "--decrypt", type=str, help="file to decrypt")
	parser.add_argument("-o", "--output", type=str, help="output file", default="output.txt")
	args = parser.parse_args()

	if args.encrypt is not None:
		encfile(args.encrypt,args.key,args.output)

	elif args.decrypt is not None:
		decfile(args.decrypt,args.key,args.output)
	else:
		print "RC4 Encryptor/Decryptor"
		print "Please rerun script with the -e or -d flag"

if __name__ == "__main__":
	main()
