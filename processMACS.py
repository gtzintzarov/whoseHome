#! /usr/bin/python

import csv
import RPi.GPIO as GPIO

class networkUser:
	def __init__(self, MAC_addr):
		self.myMAC = MAC_addr

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)


MACSonNET = []
Edwin = '18:af:61:07:1e:84'
George = 'd4:f4:6f:1e:bd:2d'
Lewis = 'b8:e8:56:a9:23:a5'
Miller = 'd4:f4:6f:3d:35:27'
amIon = False
iii = 1
with open('MACS', 'rb') as csvfile:
	MACreader = csv.reader(csvfile, delimiter='\t')
	for row in MACreader:
		if iii < 3:
			iii = iii +1
			continue
		if row.__len__() == 0:
			break
		MACSonNET.append(networkUser(row[1]))
		if George != row[1]:
			continue
		if George == row[1]:
			amIon = True
			break
	if amIon:
		#print('George is online')
		GPIO.output(13, GPIO.HIGH)
	else:
		#print('George is offline')
		GPIO.output(13, GPIO.LOW)
