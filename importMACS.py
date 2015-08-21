#! /usr/bin/python

import csv
#import RPi.GPIO as GPIO

class networkUser:
	def __init__(self, MAC_addr):
		self.myMAC = MAC_addr

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(13, GPIO.OUT)


MACSonNET = []
Edwin = '18:af:61:07:1e:84'
George = 'd4:f4:6f:1e:bd:2d'
amIon = False
with open('MACS', 'rb') as csvfile:
	MACreader = csv.reader(csvfile, delimiter=' ')
	for row in MACreader:
		MACSonNET.append(networkUser(row[3]))
		if George != row[3]:
			continue
		if George == row[3]:
			#GPIO.output(13, GPIO.HIGH)
			amIon = True
			break
	if amIon:
		print('George is online')
	else:
		print('George is offline')
