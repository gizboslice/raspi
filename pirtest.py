

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)      #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)      #LED output pin

while True:
	i = GPIO.input(11)
	if i == 0:               #when output from motion sensor is LOW
		print "No intruders", i
		GPIO.output(3, 0)    #turn light off
		time.sleep(0.1)
	elif i == 1:             #when output from motion sensor is HIGH
		print "Intruder detected", i
		GPIO.output(3, 1)    #turn light on
		time.sleep(0.1)