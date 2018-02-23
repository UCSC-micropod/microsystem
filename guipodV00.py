##------------------------------------------------------------------------------
# This is super prototype/beta for the microsystem for the micropod.
# I'm "trying" to make it as modular as possible.
#
#   The GUIWindow section is basically done. Probably don't mess with it(:
#   WIDGET BUTTONS section is pretty much done. Go ahead and edit/add buttons tho
#   Main thing to work on are the different frames/pages
#       do w/e you want. To have that page show, run and click the button
#       corresponding to the page. I currently only have the first 3 working.
#   add functions as needed.
##IMPORTS-----------------------------------------------------------------------
# from PIL import Image   #gonna be to resize image, altho.. idk how to make work
from tkinter import *
import tkinter.font
# import RPi.GPIO   //uncomment if using pi
##GUIWindow---don't edit it if can help it--------------------------------------
window = tkinter.Tk()
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()
window.geometry('%dx%d' % (screen_w, screen_h))
window.title("podhubV00")
def toggle_fullscreen(event):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))

def close(event):
    # RPi.GPIO.cleanup()    // use if using the pi
    window.destroy()

window.bind('<F12>', toggle_fullscreen)
window.bind('<F11>', close)
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
##functions --------------------------------------------------------------------
def switch_HOME():
    frame_LEDS.pack_forget()
    frame_SETT.pack_forget()
    btn_HOME.configure(relief=SUNKEN)
    btn_LEDS.configure(relief=FLAT)
    btn_SETT.configure(relief=FLAT)
    frame_HOME.pack(fill=BOTH, side=LEFT, expand=True)

def switch_LEDS():
    frame_HOME.pack_forget()
    frame_SETT.pack_forget()
    btn_HOME.configure(relief=RAISED)
    btn_LEDS.configure(relief=SUNKEN)
    btn_SETT.configure(relief=RAISED)
    frame_LEDS.pack(fill=BOTH, side=LEFT, expand=True)

def switch_SETT():
    frame_HOME.pack_forget()
    frame_LEDS.pack_forget()
    btn_HOME.configure(relief=RAISED)
    btn_LEDS.configure(relief=RAISED)
    btn_SETT.configure(relief=SUNKEN)
    frame_SETT.pack(fill=BOTH, side=LEFT, expand=True)

##WIDGET_BottomButtons---can change/add more buttons---if add, update number_of_buttons--------
bot_frame = Frame(window)
bot_frame.pack(side=BOTTOM, fill=X)
h=6
number_of_buttons = 3

btn_HOME = Button(bot_frame, command=switch_HOME, text="Home", font=myFont, bg='green', fg='white', height=h, relief=SUNKEN, pady=0, padx=2)
btn_HOME.grid(row=0, column=0, sticky='we')
btn_LEDS = Button(bot_frame, command=switch_LEDS, text="LEDS", font=myFont, bg='black', fg='green', height=h, relief=RAISED, pady=0, padx=2)
btn_LEDS.grid(row=0, column=1, sticky='we')
btn_SETT = Button(bot_frame, command=switch_SETT, text="Settings", font=myFont, bg='bisque2', fg='#000000', height=h, relief=RAISED, pady=0, padx=2)
btn_SETT.grid(row=0, column=2, sticky="we")
# btn_idk1 = Button(bot_frame, text="idk1", font=myFont, bg='red', fg='white', height=h, relief=RAISED)
# btn_idk1.grid(row=0, column=3, sticky="we")
# btn_idk2 = Button(bot_frame, text="idk2", font=myFont, bg='red', fg='white', height=h, relief=RAISED)
# btn_idk2.grid(row=0, column=4, sticky="we")

for i in range(0,number_of_buttons):
    bot_frame.columnconfigure(i, weight=1)
## home page  ------------------------------------------------------------------
frame_HOME = Frame(window, bg='green')
frame_HOME.pack(fill=BOTH, side=LEFT, expand=True)

## led page --------------------------------------------------------------------
frame_LEDS = Frame(window, bg='black')


## settings page ---------------------------------------------------------------
frame_SETT = Frame(window, bg='bisque2')


## whatever page ---------------------------------------------------------------


## whatever page ---------------------------------------------------------------


#-------------------------------------------------------------------------------
# hi.

##------------------------------------------------------------------------------

window.mainloop()
