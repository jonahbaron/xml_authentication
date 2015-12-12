#!/usr/bin/env python

import xml.etree.ElementTree as ET
import argparse

def main():
	parser = argparse.ArgumentParser(description="Parse an XML file")
	parser.add_argument("xmlfile", type=str, help="xml file to parse")
	args = parser.parse_args()

	f = args.xmlfile

	tree = ET.parse(f)
	root = tree.getroot()
	#root = ET.fromstring(user_data_as_string)

	for child in root:
		uname = child.find('name').text
		password = child.find('password').text
		permission = child.find('permission').text
		data = uname + "|||" + password + "|||" + permission
		print data
	print ""

if __name__ == "__main__":
	main()
