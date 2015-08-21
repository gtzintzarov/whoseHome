#! /usr/bin/python

import csv
import RPi.GPIO as GPIO

class networkUser:
	def __init__(self, MAC_addr):
		self.myMAC = MAC_addr

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)


MACSonNET = []
Edwin = 'a4:5e:60:cb:4e:43'

with open('MACS', 'rb') as csvfile:
	MACreader = csv.reader(csvfile, delimiter=' ')
	for row in MACreader:
		MACSonNET.append(networkUser(row[3]))
		if Edwin == row[3]:
			GPIO.output(13, GPIO.HIGH)
