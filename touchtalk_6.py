#client Mode setup
import Adafruit_GPIO as GPIO
#gpio = GPIO.get_platform_gpio()
#import RPi.GPIO as GPIO
import time
import signal

from mode_operation_6 import *
from display_fcns_4 import *
from setup_images import *

#Page buttons
Bp1 = 0 #18 10/9/17
Bp2 = 23
Bp3 = 24
Bp4 = 25

#Grid buttons
Bg1 = 12
Bg2 = 16
Bg3 = 6 #20 SPI 1 MOSI
Bg4 = 13 #21 SPI 1 CLK

#Mode select
global client_latch
client_latch = 15
global staff_latch
staff_latch = 14
global audio_latch
audio_latch = 19
global image_latch
image_latch = 3

#global variables
global page_select
page_select = 1

global current_mode
global page_num

global staff_mode
staff_mode = 0 #default is audio mode

global image_select
image_select=0

debounce_time=1000 #milliseconds
global counter
counter =0

global path0
path0 = "/home/pi/touchtalk/image_library/"

################################################################################
def determine_mode(start):
    #Mode select
    global current_mode
    time.sleep(0.1)
    if not gpio.input(client_latch) and gpio.input(staff_latch):
        current_mode = 0 #client mode
        print("Switching to Client Mode")
        page_input(page_select,start)
        image_select_write(0)
        grid_select_write(0) #reset for next image mode
        
    elif not gpio.input(staff_latch) and gpio.input(client_latch): #turn the switch to staff mode and image/audio mode
        current_mode = 1 #Staff mode
        print("Switching to Staff Mode")
        page_input(page_select,start)
        if (gpio.input(audio_latch) == 0):
        	staff_mode_audio()
        	image_select_write(0)
        	grid_select_write(0) #reset for next image mode
        elif (gpio.input(image_latch) == 0):
        	staff_mode_image()
        
###################################################################################################
        ##########################################
def page_input(page_num,start):
	time.sleep(0.1)
	image_select = image_select_read()
	global counter
	
	if (image_select==0):
		global page_select
		if (not gpio.input(Bp1) or start):
			print('button _page_1_ pressed')
			page_select = 1
			set_page(1)
        
		elif (not gpio.input(Bp2)):
			print('button _page_2_ pressed')
			page_select = 2
			set_page(2)

		elif (not gpio.input(Bp3)):
			print('button _page_3_ pressed')
			page_select = 3
			set_page(3)
        
		elif (not gpio.input(Bp4)):
			print('button _page_4_ pressed')
			page_select = 4
			set_page(4)
	else:
		grid_select=grid_select_read()
		
		min_image =0
		max_image = max_image_number()
		image_array = myimages_name()
		if (not gpio.input(Bp1) or start):
                    print('button _page_1_ pressed')
                    #page_select = 1
                    if(counter < max_image):
                        counter += 1
                        print(counter)
                        print('increment counter') 
                    elif(counter == max_image):
                        counter = min_image
                        print(counter)
			# send he counter the display the image
                    #image_array = myimages_name()
                    display_image_staff(grid_select,path0+image_array[counter])
        
		elif (not gpio.input(Bp2)):
                    print('button _page_2_ pressed')
                    #page_select = 2
                    if(counter > min_image):
                        counter -= 1
                        print(counter)
                        print('decrement counter') 
                    elif(counter == min_image):
                        counter = max_image
                        print(counter)
                    #image_array = myimages_name()
                    display_image_staff(grid_select,path0+image_array[counter])
			

		elif (not gpio.input(Bp3)):
                    print('button _page_3_ pressed')
                    image_save(grid_select,page_select,counter)
			
        
		elif (not gpio.input(Bp4)):
                    image_select_write(0) # cancel image selection
                    #page_select = 4
			
#####################################
#Staff mode       
def staff_mode_audio():
	time.sleep(0.01)
	image_select_write(0)
	global staff_mode
	if  not gpio.input(audio_latch) and gpio.input(image_latch):
		staff_mode=0;
		print('You are in audio setup')
		print(staff_mode)
	
    
def staff_mode_image():
	time.sleep(0.01)
	global staff_mode
	if not gpio.input(image_latch) and gpio.input(audio_latch):
		staff_mode=1;
		print('You are in image setup')
		#print(staff_mode)
    
	##turn the switch to staff mode and then to image mode
	#select the page you want to change the images on it
    #page_input(page_select) #uncomment this
	#select the Bg you want to change the image on it
	#page buttons become special functions (increment, decrement, save, cancel)
	#when you hit cancel=Bp4 and/or save=Bp3 the page buttons go back to their normal use (page selection)
	#select the Bg and the image will flash (display and not display)
	#from the page buttons 1 and 2 scroll down and up the images 
	#the page button 3 for save and 4 for cancel
	#index decrease when Pb1 pressed
	#index increase when Pb2 pressed



gpio.cleanup()
gpio = GPIO.get_platform_gpio()
#Page buttons
gpio.setup(Bp1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(Bp2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(Bp4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(Bp3,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Grid buttons
gpio.setup(Bg1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(Bg2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(Bg3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(Bg4,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Mode latches
gpio.setup(client_latch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(staff_latch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(image_latch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
gpio.setup(audio_latch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

gpio.add_event_detect(client_latch, GPIO.FALLING, callback = lambda x: determine_mode(0), bouncetime=3000)
gpio.add_event_detect(staff_latch, GPIO.FALLING, callback = lambda x: determine_mode(0), bouncetime=3000)
gpio.add_event_detect(image_latch, GPIO.FALLING, callback = lambda x: staff_mode_image(), bouncetime=3000)
gpio.add_event_detect(audio_latch, GPIO.FALLING, callback = lambda x: staff_mode_audio(), bouncetime=3000)


gpio.add_event_detect(Bp1, GPIO.FALLING, callback = lambda x: page_input(1,0), bouncetime=debounce_time)
gpio.add_event_detect(Bp2, GPIO.FALLING, callback = lambda x: page_input(2,0), bouncetime=debounce_time)
gpio.add_event_detect(Bp3, GPIO.FALLING, callback = lambda x: page_input(3,0), bouncetime=debounce_time)
gpio.add_event_detect(Bp4, GPIO.FALLING, callback = lambda x: page_input(4,0), bouncetime=debounce_time)
    
gpio.add_event_detect(Bg1, GPIO.FALLING, callback = lambda x:grid_input(1,page_select,current_mode,staff_mode), bouncetime=debounce_time)
gpio.add_event_detect(Bg2, GPIO.FALLING, callback = lambda x:grid_input(2,page_select,current_mode,staff_mode), bouncetime=debounce_time)
gpio.add_event_detect(Bg3, GPIO.FALLING, callback = lambda x:grid_input(3,page_select,current_mode,staff_mode), bouncetime=debounce_time)
gpio.add_event_detect(Bg4, GPIO.FALLING, callback = lambda x:grid_input(4,page_select,current_mode,staff_mode), bouncetime=debounce_time)


determine_mode(1) # grab default state


try:
    while True:
        signal.pause()


except KeyboardInterrupt:
    gpio.cleanup()
