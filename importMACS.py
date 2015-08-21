#! /usr/bin/python

import csv


with open('MACS', 'rb') as csvfile:
	MACreader = csv.reader(csvfile, delimiter=' ')
	for row in MACreader:
		print row[3]

