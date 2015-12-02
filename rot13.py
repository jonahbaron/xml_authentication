#!/usr/bin/env python

import string
import argparse

def rot13(text1):
	rot = string.maketrans(
		"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
		"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

	text2 = string.translate(text1, rot)

	return text2

def main():
	parser = argparse.ArgumentParser(description='Encrypt or decrypt a string')
	parser.add_argument("string", type=str, help="encrypt or decrypt entered string (ROT13 encryption = ROT13 decryption)")
	args = parser.parse_args()

	print "ROT13 Encryptor/Decryptor"
	print ""

	print args.string
	newstring = rot13(args.string)
	print newstring


if __name__ == "__main__":
	main()
