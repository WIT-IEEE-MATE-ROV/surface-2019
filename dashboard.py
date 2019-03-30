import tkinter as tk
import dashboardutils as dbu
from PIL import ImageTk, Image
from subprocess import Popen, PIPE

root = tk.Tk()
root.geometry("900x600")
CONTENT_FONT_SIZE = 10

##
# Set up basic layout
##

# Start by establishing some frames
titlebar_frame = tk.Frame(root, bd=1, relief="sunken")
forwardvideo_frame = tk.Frame(root, bd=1, relief="sunken")
bottomvideo_frame = tk.Frame(root, bd=1, relief="sunken")
button_frame = tk.Frame(root, bd=1, relief="sunken")
data_frame = tk.Frame(root, bd=1, relief="sunken")
log_frame = tk.Frame(root, bd=1, relief="sunken")

# Now the positions of those frames
titlebar_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)
forwardvideo_frame.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
bottomvideo_frame.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
button_frame.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
data_frame.grid(row=1, column=1, rowspan=3, sticky="nsew", padx=2, pady=2)
log_frame.grid(row=1, column=2, rowspan=3, sticky="nsew", padx=2, pady=2)

# With positions set up, handle sizing of rows/columns
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=0)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)

log_frame.grid_rowconfigure(0, weight=0)

###
## Start filling content
###

##
# Top bar- the logo and title
##
logoimage = ImageTk.PhotoImage(Image.open("./assets/nuglogo.png")
                               .resize((100, 100), Image.ANTIALIAS))

logo = tk.Label(titlebar_frame, image=logoimage)
logo.grid(column=0, row=0)
title = tk.Label(titlebar_frame, text="Nugget Industries ROV (dashboard v0.3 alpha)", font=("Roboto", 25))
title.grid(column=1, row=0)

##
# Left bar- video and stuff
##
# TODO: MAKE THIS NOT JUST BE AN IMAGE
#                                           lol
fvideo = ImageTk.PhotoImage(Image.open("./assets/novid.png").resize((520, 400), Image.ANTIALIAS))
l_fvideo = tk.Label(forwardvideo_frame, image=fvideo).grid(column=0, row=0)

bvideo = ImageTk.PhotoImage(Image.open("./assets/novid.png").resize((520, 400), Image.ANTIALIAS))
l_bvideo = tk.Label(bottomvideo_frame, image=fvideo).grid(column=0, row=0)

# TODO: MAKE THIS NOT JUST BE AN IMAGE
rollimg_ghost = ImageTk.PhotoImage(Image.open("./assets/rovback_ghost.png").resize((400, 400), Image.ANTIALIAS))
l_rollimg_ghost = tk.Label(forwardvideo_frame, image=rollimg_ghost).grid(column=1, row=0)

pitchimg = ImageTk.PhotoImage(Image.open("./assets/rovside_ghost.png").resize((400, 400), Image.ANTIALIAS))
l_pitchimg = tk.Label(bottomvideo_frame, image=pitchimg).grid(column=1, row=0)

tk.Button(button_frame, text="Start line tracking",   command=dbu.start_line_track  ).grid(column=0, row=0)
tk.Button(button_frame, text="Measure Cannon",        command=dbu.measure_cannon    ).grid(column=1, row=0)
tk.Button(button_frame, text="Count Benthic Species", command=dbu.count_benthic     ).grid(column=2, row=0)
tk.Button(button_frame, text="Open PID Tuning",       command=dbu.open_pid          ).grid(column=3, row=0)
tk.Button(button_frame, text="Open SSH Terminal",     command=dbu.open_ssh          ).grid(column=4, row=0)
# tk.Button(button_frame, text="ROV Mem",               command=dbu.open_rov_mem      ).grid(column=5, row=0)
# tk.Button(button_frame, text="PC Mem",                command=dbu.open_pc_mem       ).grid(column=6, row=0)
tk.Button(button_frame, text="Shutdown ROV",          command=dbu.shutdown_rov      ).grid(column=7, row=0)
tk.Button(button_frame, text="Shutdown All",          command=dbu.shutdown          ).grid(column=8, row=0)

##
# Sensor/system/joystick data
##
# Header
tk.Label(data_frame, text="  Sensor  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=0, row=0)
tk.Label(data_frame, text="  Value  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=1, row=0)

# Content
tk.Label(data_frame, text="pH", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=1)
tk.Label(data_frame, text="IR", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=2)
tk.Label(data_frame, text="Depth", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=3)
tk.Label(data_frame, text="Temp", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=4)

# Header
tk.Label(data_frame, text="  System  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=0, row=5)
tk.Label(data_frame, text="  Value   ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=1, row=5)

# Content
tk.Label(data_frame, text="T1", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=7)
tk.Label(data_frame, text="T2", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=8)
tk.Label(data_frame, text="T3", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=9)
tk.Label(data_frame, text="T4", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=10)
tk.Label(data_frame, text="T5", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=11)
tk.Label(data_frame, text="T6", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=12)
tk.Label(data_frame, text="T7", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=13)
tk.Label(data_frame, text="T8", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=14)
tk.Label(data_frame, text="Manip", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=15)
tk.Label(data_frame, text="Dumper", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=16)
tk.Label(data_frame, text="Probe", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=17)

# Header
tk.Label(data_frame, text="  Axis  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=0, row=19)
tk.Label(data_frame, text="  Value  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=1, row=19)

# Content
tk.Label(data_frame, text="X", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=21)
tk.Label(data_frame, text="Y", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=22)
tk.Label(data_frame, text="T", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=23)
tk.Label(data_frame, text="L", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=24)

# Header
tk.Label(data_frame, text="  Button  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=0, row=25)
tk.Label(data_frame, text="  On/Off  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=1, row=25)

# Content
tk.Label(data_frame, text="1", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=26)
tk.Label(data_frame, text="2", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=27)
tk.Label(data_frame, text="3", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=28)
tk.Label(data_frame, text="4", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=29)
tk.Label(data_frame, text="5", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=30)
tk.Label(data_frame, text="6", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=31)
tk.Label(data_frame, text="7", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=32)
tk.Label(data_frame, text="8", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=33)
tk.Label(data_frame, text="9", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=34)
tk.Label(data_frame, text="10", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=35)
tk.Label(data_frame, text="11", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=36)
tk.Label(data_frame, text="12", font=("Roboto", CONTENT_FONT_SIZE)).grid(column=0, row=37)

##
# The log thingy
##
tk.Label(log_frame, text="  LOG  ", font=("Roboto", CONTENT_FONT_SIZE+5)).grid(column=0, row=0)
logtext = tk.Text(log_frame, height=50)
logtext.insert(tk.END, "Logging ready to start!\n")
logtext.insert(tk.END, "Waiting on the user to connect.\n")

p = Popen(["tail", "-60", "./surfacelog.txt"], shell=False, stderr=PIPE, stdout=PIPE)
res, err = p.communicate()
if not err:
    lastsixty = res.decode()
    logtext.insert(tk.END, "{:s}\n".format(lastsixty))

logtext.grid(column=0, row=1, sticky="nsew")


# dataframe_update(data_frame)
# logframe_update(logtext)
dbu.dataframe_update(data_frame)
root.mainloop()