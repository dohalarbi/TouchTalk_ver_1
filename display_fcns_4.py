# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from PIL import Image

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
gpio = GPIO.get_platform_gpio()
import Adafruit_GPIO.SPI as SPI
import os
import time

global cs1, cs2, cs3, cs4
cs1 = 20
cs2 = 21
cs3 = 18
cs4 = 17

#reset pins
global rst1,rst2, rst3, rst4
rst1 = 2
rst2 = 27
rst3 = 22
rst4 = 26
    
def display_image(page_select,grid_select):
	
	image_path2 = "/home/pi/touchtalk"
	if  (page_select == 1):
		image_path2 = image_path2 + "/Page_1"
	elif(page_select == 2):
		image_path2 = image_path2 + "/Page_2"
	elif(page_select == 3):
		image_path2 = image_path2 + "/Page_3"
	elif(page_select == 4):
		image_path2 = image_path2 + "/Page_4"
	
	if  (grid_select == 1):
		image_path2 = image_path2 + "/Grid_1/"
		cs=cs1
		reset=rst1
		port_num=0
		dev_num=0
		
	elif (grid_select == 2):
		image_path2 = image_path2 + "/Grid_2/"
		cs=cs2
		reset=rst2
		port_num=0
		dev_num=1
		
	elif (grid_select == 3):
		image_path2 = image_path2 + "/Grid_3/"
		cs=cs3
		reset=rst3
		port_num=0
		dev_num=0
		
	elif (grid_select == 4):
		image_path2 = image_path2 + "/Grid_4/"
		cs=cs4
		reset=rst4
		port_num=0
		dev_num=1
		
	image_path2 = image_path2 + "image.jpg"
	
	gpio.setup(cs, GPIO.OUT) #cs: 27,2, , 
	gpio.output(cs, GPIO.HIGH)
	
	# Raspberry Pi configuration.
	DC = 4 
	RST = reset #rst: 17,22, ,
	SPI_PORT = port_num
	SPI_DEVICE = dev_num
	
	# Create TFT LCD display class.
	disp1 = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=640))
	#disp1 = TFT.ILI9341(DC, rst=RST, spi=SPI.BitBang(gpio,11,mosi=10, miso=None, ss=cs))
	# Initialize display.
	
	gpio.output(cs, GPIO.LOW)
	disp1.begin()
	gpio.output(cs, GPIO.HIGH)
	
	# Load an image.
	print('Loading image...')
	image = Image.open(image_path2)
	
	# Resize the image and rotate it so it's 240x320 pixels.
	image = image.rotate(180).resize((240, 320))
	
	# Draw the image on the display hardware.
	print('Drawing image')
	gpio.output(cs, GPIO.LOW)
	disp1.display(image)
	gpio.output(cs, GPIO.HIGH)

def display_image_staff(grid_select,path):
	
	if  (grid_select == 1):
		cs=cs1
		reset=rst1
		port_num=0
		dev_num=0
		
	elif (grid_select == 2):
		cs=cs2
		reset=rst2
		port_num=0
		dev_num=1
		
	elif (grid_select == 3):
		cs=cs3
		reset=rst3
		port_num=0
		dev_num=0
		
	elif (grid_select == 4):
		cs=cs4
		reset=rst4
		port_num=0
		dev_num=1
	
	gpio.setup(cs, GPIO.OUT) #cs: 27,2, , 
	gpio.output(cs, GPIO.HIGH)
	
	# Raspberry Pi configuration.
	DC = 4 
	RST = reset #rst: 17,22, ,
	SPI_PORT = port_num
	SPI_DEVICE = dev_num
	
	# Create TFT LCD display class.
	disp1 = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=640))
	
	# Initialize display.
	
	gpio.output(cs, GPIO.LOW)
	disp1.begin()
	gpio.output(cs, GPIO.HIGH)
	
	# Load an image.
	print('Loading image...')
	image = Image.open(path)
	
	# Resize the image and rotate it so it's 240x320 pixels.
	image = image.rotate(180).resize((240, 320))
	
	# Draw the image on the display hardware.
	print('Drawing image')
	gpio.output(cs, GPIO.LOW)
	disp1.display(image)
	gpio.output(cs, GPIO.HIGH)

def flash(page_select,grid_select):
	for i in range(1,4):
		display_image(page_select,grid_select)
		time.sleep(0.5)

def set_page(page):
	if page == 1 :
		display_image(page, 1)
		time.sleep(0.25)
		display_image(page, 2)
		time.sleep(0.25)
		display_image(page, 3)
		time.sleep(0.25)
		display_image(page, 4)
	elif page == 2 :
		display_image(page, 1)
		time.sleep(0.25)
		display_image(page, 2)
		time.sleep(0.25)
		display_image(page, 3)
		time.sleep(0.25)
		display_image(page, 4)
	elif page == 3:
		display_image(page, 1)
		time.sleep(0.25)
		display_image(page, 2)
		time.sleep(0.25)
		display_image(page, 3)
		time.sleep(0.25)
		display_image(page, 4)
	else:
		display_image(page, 1)
		time.sleep(0.25)
		display_image(page, 2)
		time.sleep(0.25)
		display_image(page, 3)
		time.sleep(0.25)
		display_image(page, 4)
