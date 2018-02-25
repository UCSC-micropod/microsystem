##==============================================================================
# This is super prototype/beta for the microsystem for the micropod.
# I'm "trying" to make it as modular as possible.
#
#   The GUIWindow section is basically done. Probably don't mess with it(:
#   WIDGET BUTTONS section is pretty much done. Go ahead and edit/add buttons tho
#   Main thing to work on are the different frames/pages
#       do w/e you want. To have that page show, run and click the button
#       corresponding to the page. I currently only have the first 3 working.
#   add functions as needed.
##==============================================================================
## IMPORTS ---------------------------------------------------------------------
##==============================================================================
from tkinter import *
import tkinter.font
from ToolsByJohn import *
import time
from PIL import Image  #gonna be to resize image, altho.. idk how to make work
# import RPi.GPIO   //uncomment if using pi
##==============================================================================
## GUIWindow---don't edit it if can help it ------------------------------------
##==============================================================================
window = tkinter.Tk()
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()
window.geometry('%dx%d' % (screen_w, screen_h))
window.title("podhubV00")
# window.resizable(False, False)
window.attributes('-fullscreen', True)
def toggle_fullscreen(event):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))

def close(event):
    # RPi.GPIO.cleanup()    // use if using the pi
    window.destroy()

window.bind('<F12>', toggle_fullscreen)
window.bind('<F11>', close)
window.bind('<F2>', toggle_fullscreen)
window.bind('<F1>', close)
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##==============================================================================
## FUNCTIONS -------------------------------------------------------------------
##==============================================================================
def switch_HOME():
    frame_LEDS.pack_forget()
    frame_SETT.pack_forget()
    btn_HOME.configure(relief=SUNKEN)
    btn_LEDS.configure(relief=RAISED)
    btn_SETT.configure(relief=RAISED)
    frame_HOME.pack(fill=BOTH, side=LEFT, expand=True)
    frame_HOME.update()

def switch_LEDS():
    frame_HOME.pack_forget()
    frame_SETT.pack_forget()
    btn_HOME.configure(relief=RAISED)
    btn_LEDS.configure(relief=SUNKEN)
    btn_SETT.configure(relief=RAISED)
    frame_LEDS.pack(fill=BOTH, side=LEFT, expand=True)
    frame_LEDS.update()

def switch_SETT():
    frame_HOME.pack_forget()
    frame_LEDS.pack_forget()
    btn_HOME.configure(relief=RAISED)
    btn_LEDS.configure(relief=RAISED)
    btn_SETT.configure(relief=SUNKEN)
    frame_SETT.pack(fill=BOTH, side=LEFT, expand=True)
    frame_HOME.update()

def clock(time1=''):
    time2= time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        label_clock.config(text=time2)
        label_clock.after(200,clock)

# def screenupdate(screen_w, screen_h, window):
#     if screen_w != window.winfo_screenwidth or screen_h != window.winfo_screenheight():
#         return window.winfo_screenwidth(), window.winfo_screenheight()

##==============================================================================
## IMAGES for the buttons! only took me 99999 hours to figure out ):
##==============================================================================
baseheight = int(screen_h/10)

img_HOME = PhotoImage(file=img_rescale_baseheight("icon/icon_home1.png", baseheight))
img_LEDS = PhotoImage(file=img_rescale_baseheight("icon/icon_leds1.png", baseheight))
img_SETT = PhotoImage(file=img_rescale_baseheight("icon/icon_sett1.png", baseheight))

##==============================================================================
## WIDGET_BottomButtons---can change/add more buttons---if add, update number_of_buttons ==
##==============================================================================
bot_frame = Frame(window)
bot_frame.pack(side=BOTTOM, fill=X)
number_of_buttons = 3

btn_HOME = Button(bot_frame, command=switch_HOME, image=img_HOME, bg='green', fg='white', relief=SUNKEN, pady=0, padx=2)
btn_HOME.grid(row=0, column=0, sticky='we')

btn_LEDS = Button(bot_frame, command=switch_LEDS, image=img_LEDS, bg='black', fg='green', relief=RAISED, pady=0, padx=2)
btn_LEDS.grid(row=0, column=1, sticky='we')

btn_SETT = Button(bot_frame, command=switch_SETT, image=img_SETT, bg='bisque2', fg='#000000', relief=RAISED, pady=0, padx=2)
btn_SETT.grid(row=0, column=2, sticky="we")

for i in range(0,number_of_buttons):
    bot_frame.columnconfigure(i, weight=1)

##==============================================================================
## home page  ------------------------------------------------------------------
##==============================================================================
frame_HOME = Frame(window, bg='green')
frame_HOME.pack(fill=BOTH, side=LEFT, expand=True)
frame_HOME.update()
image = PhotoImage(file=img_rescale_baseheight("pics/4ktest4k.jpg", frame_HOME.winfo_height()))

label_bg = Label(frame_HOME, image=image, padx=0, pady=0)
label_bg.grid(row=0,column=0, sticky='w')

label_clock = Label(frame_HOME, font=('times', 100, 'bold'), bg='#06A5FB')
label_clock.grid(row=0, column=0, sticky='n')

clock()

##==============================================================================
## led page --------------------------------------------------------------------
##==============================================================================
frame_LEDS = Frame(window, bg='black')

##==============================================================================
## settings page ---------------------------------------------------------------
##==============================================================================
frame_SETT = Frame(window, bg='bisque2')

##==============================================================================
## whatever page ---------------------------------------------------------------
##==============================================================================

##==============================================================================
## whatever page ---------------------------------------------------------------
##==============================================================================


#-------------------------------------------------------------------------------
# hi.

##------------------------------------------------------------------------------

# screen_w, screen_h = screenupdate(screen_w, screen_h, window)
window.mainloop()
