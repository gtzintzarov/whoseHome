#! /usr/bin/python

import csv
import currentNetwork

myMACS = []
with open('MACS', 'rb') as csvfile:
	MACreader = csv.reader(csvfile, delimiter=' ')
	for row in MACreader:
		myMACS.append(networkUser(row[3]))
		print row[3]

