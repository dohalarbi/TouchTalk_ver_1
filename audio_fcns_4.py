import Adafruit_GPIO as GPIO
gpio = GPIO.get_platform_gpio()
import os
import subprocess
import psutil
import time

def record(page_select,grid_select):
	Bg1 = 12
	Bg2 = 16
	Bg3 = 6 #20 SPI 1 MOSI
	Bg4 = 13 #21 SPI 1 CLK
	gpio = GPIO.get_platform_gpio()

	procname = 'arecord'

	recording = 0 #default state
	killed = 0
	######
	fname = "/home/pi/touchtalk"
	if  (page_select == 1):
		fname = fname + "/Page_1"
	elif(page_select == 2):
		fname = fname + "/Page_2"
	elif(page_select == 3):
		fname = fname + "/Page_3"
	elif(page_select == 4):
		fname = fname + "/Page_4"
	
	if  (grid_select == 1):
		fname = fname + "/Grid_1/"
		grid_select = Bg1
	elif (grid_select == 2):
		fname = fname + "/Grid_2/"
		grid_select = Bg2
	elif (grid_select == 3):
		fname = fname + "/Grid_3/"
		grid_select = Bg3
	elif (grid_select == 4):
		fname = fname + "/Grid_4/"
		grid_select = Bg4
	
	fname = fname + "recording.wav"
	
	rec_string = "arecord -f S16_LE -t wav -c 2 -d 10 -Dplug:default " + fname
	play_string = "aplay -f S16_LE -t wav -c 2 -d 10 -Dplug:default " + fname
	######
	
	gpio.setup(grid_select, GPIO.IN, pull_up_down=GPIO.PUD_UP) #grid button 1
	
	try:

		while True:
			if (gpio.input(grid_select)==0 and recording == 0): #press grid switch to start recording
				process = subprocess.Popen(rec_string, shell=True)
				print ("recording")
				recording = 1
				#time.sleep(11)

			if (gpio.input(grid_select)==1 and recording == 1): #grid switch has been released and recording is done
				print ("recording stopped")
				os.system('pkill arecord')
				print('Playback in 5 seconds')
				time.sleep(1)
				process = subprocess.Popen(play_string, shell=True)
				killed=1;
		    

			if (recording and killed == 1):
				print("break")
				recording = 0
				killed = 0
				break

	except KeyboardInterrupt:
		gpio.cleanup()


def audio_playback(page_select,grid_select):
    fname = "/home/pi/touchtalk"
    if  (page_select == 1):
        fname = fname + "/Page_1"
    elif(page_select == 2):
        fname = fname + "/Page_2"
    elif(page_select == 3):
        fname = fname + "/Page_3"
    elif(page_select == 4):
        fname = fname + "/Page_4"
        
    if  (grid_select == 1):
        fname = fname + "/Grid_1/"
    elif (grid_select == 2):
        fname = fname + "/Grid_2/"
    elif (grid_select == 3):
        fname = fname + "/Grid_3/"
    elif (grid_select == 4):
        fname = fname + "/Grid_4/"
        
    fname = fname + "recording.wav"
        
    popen_string = "aplay -f S16_LE -t wav -c 2 -d 10 -Dplug:default " + fname
    process = subprocess.Popen(popen_string, shell=True)
