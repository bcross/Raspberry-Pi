"""
How To Use
1. Start python where piled.py is located.
2. Run "from piled import *" or "import piled"
3. My red LED is plugged into GPIO port 7 so I run "red = Led(7)" or "red = piled.Led(7) depending on what was run in step 2
4. Have fun!  check the code for what the object is capable of.
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class Led():
	
	#initialize the class.
	def __init__(self,ionum):
		self.current = 0
		#set the specified GPIO pin to output type
		GPIO.setup(ionum, GPIO.OUT)
		#make the led object PWM driver for that pin with a maximum duty cycle of 100 (which is max for PWM)
		self.led = GPIO.PWM(ionum, 100)
		#start the led PWM with a duty cycle of 0
		self.led.start(0)

	#brighten the LED
	def up(self,brightness='no',rate=0.008):
		if brightness == 'no': brightness = 100
		self.change(brightness)

	#dim the LED
	def down(self,brightness='no',rate=0.008):
		if brightness == 'no': brightness = -100
		self.change(brightness)

	#change the brightness of the LED
	def change(self,change,rate = 0.008):
		if change > 0:
			while change != 0:
				if self.current == 100:
					print 'Cannot set duty cycle over 100'
					break
				self.current += 1
				self.led.ChangeDutyCycle(self.current)
				change -= 1
				time.sleep(rate)
			return
		if change < 0:
			while change != 0:
				if self.current == 0:
					print 'Cannot set duty cycle under 0'
					break
				self.current -= 1
				self.led.ChangeDutyCycle(self.current)
				change += 1
				time.sleep(rate)
			return

	#blink the LED
	def blink(self,blinkrate=1,holdhigh=0.05,faderate=0.008):
		self.led.ChangeDutyCycle(0)
		n = 0
		print 'Press Ctrl-C to stop'
		while True:
			try:
				self.change(100,faderate)
				time.sleep(holdhigh)
				self.change(-100,faderate)
				time.sleep(blinkrate)
			except KeyboardInterrupt:
				self.current = 0
				self.led.ChangeDutyCycle(self.current)
				break