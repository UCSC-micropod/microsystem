from tkinter import *
import tkinter.font
import time
from PIL import Image

def img_rescale_baseheight(s, baseheight):
    # this function is for the icons! its a bit weird but
    # make sure the icon has file name icon_ followed by 4 letters and 1 number
    # i mean.. i could change it but i like it. LOL(:
    img = Image.open(s)
    hpercent = (baseheight/float(img.size[1]))
    width = int((float(img.size[0])*float(hpercent)))
    img = img.resize((width, baseheight), Image.ANTIALIAS)
    s2 = s[:14] + "_resized.png"
    img.save(s2)
    return s2

def img_rescale(s, width, height):
    img = Image.open(s)
    img = img.resize((width, height), Image.ANTIALIAS)
    s2 = s[:14] + "_resized.png"
    img.save(s2)
    return s2

def img_show(img):
    img.show()

def img_prop(img):  # opens a window containing image properties
    s = img.size
    f = img.format
    string = "Size: (%d x %d)\nFormat: %s"%(s[0], s[1], f)
    window = Tk()
    window.title("Image Properties")
    label = Label(window, text = string, font=('times', 100, 'bold'), bg='black', fg='green')
    label.pack()

# def readSensor_DHT():
    # h,t = MyDHT.read_retry(dht.DHT22,20)
    # temp = "%.1f" %t
    # temperature.set(temp+ "°C"")
    # hum = "%.1f" %h
	# humidity.set(hum+"  %")
