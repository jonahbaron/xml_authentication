#!/usr/bin/env python

import argparse
import subprocess
import sys

def parseContent(f):
	pcontent = []
	command = "./xmlauthparser.py " + f
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

	while True:
		line = process.stdout.readline()
		if line != "":
			pcontent.append(line)
		else:
			break

#	with open(fauth, 'r') as f:
#		pcontent = f.readlines()

	pdata = []
	for content in pcontent:
		content = content.strip()
		plist = content.split("|||")
		pdata.append(plist)

	return pdata

def encPass(password):
	command = "./rot13.py -s " + password
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

	epass = process.stdout.readline()
	epass = epass.strip()

	return epass

def authenticate(pdata,uname,password):
	perm = 0
	for plist in pdata:
		if uname in plist and password in plist:
			perm = plist[2]
			perm = int(perm)
			return perm
	return perm

def main():
	parser = argparse.ArgumentParser(description="Enter a username and password to authenticate")
	parser.add_argument("username", type=str, help="username to authenticate")
	parser.add_argument("password", type=str, help="password to authenticate")
	parser.add_argument("-f", "--fileauth", type=str, help="file used to evaluate entered credentials", default="userauth.xml")
	parser.add_argument("-e", "--encfile", type=str, help="file to encrypt")
	parser.add_argument("-d", "--decfile", type=str, help="file to decrypt")
	args = parser.parse_args()

	uname = args.username
	password = args.password
	fauth = args.fileauth

	pdata = parseContent(fauth)
	epass = encPass(password)
	perm = authenticate(pdata,uname,epass)

	if perm > 0:
		print "Authenticated sucessfully"
	else:
		print "Authenticated unsuccessfully"
		exit(0)

	if args.encfile is not None:
		encfile = args.encfile
		if perm == 3 or perm == 2:
			print "Encrypting", encfile
			command = "./rot13.py -f " + encfile
			subprocess.Popen(command, shell=True)
			print "Check output.txt"
		else:
			print uname, "does not have permission to encrypt"
	elif args.decfile is not None:
		decfile = args.decfile
		if perm == 3 or perm == 1:
			print "Decrypting", decfile
			command = "./rot13.py -f " + decfile
			subprocess.Popen(command, shell=True)
			print "Check output.txt"
		else:
			print uname, "does not have permission to decrypt"
	else:
		print "No file encryption or decryption selected"

if __name__ == "__main__":
	main()
