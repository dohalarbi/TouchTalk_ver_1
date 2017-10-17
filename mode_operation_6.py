import Adafruit_GPIO as GPIO
from audio_fcns_4 import *
from display_fcns_4 import *
#from image_set_mode import *
import os

#####
#image chip_selects
global cs1, cs2, cs3, cs4
cs1 = 8
cs2 = 7
cs3 = 18
cs4 = 17

#reset pins
global rst1,rst2, rst3, rst4
rst1 = 2
rst2 = 27
rst3 = 22
rst4 = 26
######

global Bg1, Bg2, Bg3, Bg4
Bg1 = 12
Bg2 = 16
Bg3 = 6 #20 SPI 1 MOSI
Bg4 = 13 #21 SPI 1 CLK


def image_select_write(num):
	file=open('image_select.txt', 'w')
	file.write(str(num))
	file.close()
	
def image_select_read():
	file=open('image_select.txt', 'rt')
	image_select=int(file.read())
	file.close()
	return image_select
	
def grid_select_write(num):
	file=open('grid_select.txt', 'w')
	file.write(str(num))
	file.close()
	
def grid_select_read():
	file=open('grid_select.txt', 'rt')
	grid_select=int(file.read())
	file.close()
	return grid_select
	
	
def button_fcn(current_mode,staff_mode,page_select,grid_select):
	if (current_mode == 0): #client mode
		audio_playback(page_select, grid_select)
		flash(page_select,grid_select)
		image_select_write(0)
	
	elif (current_mode == 1): #staff mode audio
		if (staff_mode == 0):
			print('Hold button down to record')
			record(page_select,grid_select)
			image_select_write(0)
		else:					#staff mode image
			print('Image setup mode')
			flash(page_select,grid_select)
			image_select_write(1)
			grid_select_write(grid_select)

#####
def grid_input(grid_select,page_select,current_mode,staff_mode):
	#Grid buttons
	#print(staff_mode)
	
	image_select = image_select_read()
	
	if (image_select == 0):
		
		if (page_select == 1): #client mode grid button set
			#Load the pictures for page 1
			if (grid_select == 1 and gpio.input(Bg1)==0):
				#play sound 1
				print('You are in page_1 picture_1')
				image_select=button_fcn(current_mode,staff_mode,1,1)
						
			if (grid_select == 2 and gpio.input(Bg2)==0):
				#play sound 2
				print('You are in page_1 picture_2')
				image_select=button_fcn(current_mode,staff_mode,1,2)
			
			if (grid_select == 3 and gpio.input(Bg3)==0):
				#play sound 3
				print('You are in page_1 picture_3')
				image_select=button_fcn(current_mode,staff_mode,1,3)
		
			if (grid_select == 4 and gpio.input(Bg4)==0):
				#play sound 4
				print('You are in page_1 picture_4')
				image_select=button_fcn(current_mode,staff_mode,1,4)
	
		elif (page_select == 2):
			#Load the pictures for page 1
			if (grid_select == 1 and gpio.input(Bg1)==0):
				#play sound 1
				print('You are in page_2 picture_1')
				image_select=button_fcn(current_mode,staff_mode,2,1)
		
			if (grid_select == 2 and gpio.input(Bg2)==0):
				#play sound 2
				print('You are in page_2 picture_2')
				image_select=button_fcn(current_mode,staff_mode,2,2)
		
			if (grid_select == 3 and gpio.input(Bg3)==0):
				#play sound 3
				print('You are in page_2 picture_3')
				image_select=button_fcn(current_mode,staff_mode,2,3)
		
			if (grid_select == 4 and gpio.input(Bg4)==0):
				#play sound 4
				print('You are in page_2 picture_4')
				image_select=button_fcn(current_mode,staff_mode,2,4)
	
		elif (page_select == 3):
			#Load the pictures for page 1
			if (grid_select == 1 and gpio.input(Bg1)==0):
				#play sound 1
				print('You are in page_3 picture_1')
				image_select=button_fcn(current_mode,staff_mode,3,1)
		
			if (grid_select == 2 and gpio.input(Bg2)==0):
				#play sound 2
				print('You are in page_3 picture_2')
				image_select=button_fcn(current_mode,staff_mode,3,2)
		
			if (grid_select == 3 and gpio.input(Bg3)==0):
				#play sound 3
				print('You are in page_3 picture_3')
				image_select=button_fcn(current_mode,staff_mode,3,3)
		
			if (grid_select == 4 and gpio.input(Bg4)==0):
				#play sound 4
				print('You are in page_3 picture_4')
				image_select=button_fcn(current_mode,staff_mode,3,4)
	
		elif (page_select == 4):
			#Load the pictures for page 1
			if (grid_select == 1 and gpio.input(Bg1)==0):
				#play sound 1
				print('You are in page_4 picture_1')
				image_select=button_fcn(current_mode,staff_mode,4,1)
		
			if (grid_select == 2 and gpio.input(Bg2)==0):
				#play sound 2
				print('You are in page_4 picture_2')
				image_select=button_fcn(current_mode,staff_mode,4,2)
		
			if (grid_select == 3 and gpio.input(Bg3)==0):
				#play sound 3
				print('You are in page_4 picture_3')
				image_select=button_fcn(current_mode,staff_mode,4,3)
			
			if (grid_select == 4 and gpio.input(Bg4)==0):
				#play sound 4
				print('You are in page_4 picture_4')
				image_select=button_fcn(current_mode,staff_mode,4,4)
	else: #staff mode grid buttons set
		#print('inside else')
		if (grid_select == 1 and gpio.input(Bg1)==0):
			grid_select_write(1)
			#print('inside 2nd condition')
			
		if (grid_select == 2 and gpio.input(Bg2)==0):
			grid_select_write(2)
			
		if (grid_select == 3 and gpio.input(Bg3)==0):
			grid_select_write(3)
			
		if (grid_select == 4 and gpio.input(Bg4)==0):
			grid_select_write(4)	
		
	return image_select
