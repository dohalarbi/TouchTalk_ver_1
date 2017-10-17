#Staff Mode image setup
from array import array
import os
from PIL import Image
import Adafruit_GPIO as GPIO
import time
import signal

from mode_operation_6 import *
from display_fcns_4 import *



path0 = "/home/pi/touchtalk/image_library/"
#path1_1 = "/home/pi/Desktop/staff_mode_copy/page1/grid_1/"
#path1_2 = "/home/pi/Desktop/staff_mode_copy/page1/grid_2/"
#path1_3 = "/home/pi/Desktop/staff_mode_copy/page1/grid_3/"
#path1_4 = "/home/pi/Desktop/staff_mode_copy/page1/grid_4/"
#path2_1 = "/home/pi/Desktop/staff_mode_copy/page2/grid_1/"
#path2_2 = "/home/pi/Desktop/staff_mode_copy/page2/grid_2/"
#path2_3 = "/home/pi/Desktop/staff_mode_copy/page2/grid_3/"
#path2_4 = "/home/pi/Desktop/staff_mode_copy/page2/grid_4/"
#path3_1 = "/home/pi/Desktop/staff_mode_copy/page3/grid_1/"
#path3_2 = "/home/pi/Desktop/staff_mode_copy/page3/grid_2/"
#path3_3 = "/home/pi/Desktop/staff_mode_copy/page3/grid_3/"
#path3_4 = "/home/pi/Desktop/staff_mode_copy/page3/grid_4/"
#path4_1 = "/home/pi/Desktop/staff_mode_copy/page4/grid_1/"
#path4_2 = "/home/pi/Desktop/staff_mode_copy/page4/grid_2/"
#path4_3 = "/home/pi/Desktop/staff_mode_copy/page4/grid_3/"
#path4_4 = "/home/pi/Desktop/staff_mode_copy/page4/grid_4/"



print('welcome to my array')

def max_image_number():
    mylist = os.listdir(path0)
    Max = len(mylist)
    return Max

def myimages_name():
        
        mylist = os.listdir(path0)
        myarray = []
        for name in mylist:
                position = mylist.index(name)
                myarray.append(name)
                
        return myarray

       
def image_save(grid_select,page_select,count): #this function is for saving the selected image to the designated folder
	image_path = "/home/pi/touchtalk"
	
	if  (page_select == 1):
		image_path = image_path + "/Page_1"
	elif(page_select == 2):
		image_path = image_path + "/Page_2"
	elif(page_select == 3):
		image_path = image_path + "/Page_3"
	elif(page_select == 4):
		image_path = image_path + "/Page_4"
	
	if  (grid_select == 1):
		image_path = image_path + "/Grid_1/"
		
	elif (grid_select == 2):
		image_path = image_path + "/Grid_2/"
		
	elif (grid_select == 3):
		image_path = image_path + "/Grid_3/"
		
	elif (grid_select == 4):
		image_path = image_path + "/Grid_4/"
	image_path = image_path + "image.jpg"
	
	image_array = myimages_name()
	myimage = Image.open(path0 + image_array[count])
	#myimage.resize((240,320))       #resize the image to fit into the screen
	myimage.save(image_path, "JPEG")
	print('saving .... ')
	flash(page_select,grid_select)




    
    


