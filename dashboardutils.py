import socket
import json
import pygame
import tkinter
import threading
import getpass
import subprocess
import sys
import os
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep

log = ""
loglen = 0
joystick_error_message_count = 0

def appendlog(string):
    global loglen
    global log
    loglen += 1
    log = "{:s}\n{:s}".format(log, string)

def getlog():
    global log
    return log

def setup_joystick():
    pygame.joystick.init()
    pygame.init()

    try:
        pygame.init()
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
    except pygame.error:
        messagebox.showerror("OH SWEET BABY JESUS", "AAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n The joystick isn't connected, reconnect it and press OK")
        os.execl(sys.executable, sys.executable, *sys.argv)

    joystick.init()
    return joystick

def send(type, val):
    if type == "JOYVAL":
        return # TODO

def staticlabels(window):
    window.title("ROV Dashboard")

    titlelabel = tkinter.Label(window, text="ROV Dashboard", font=("Ariel Bold", 25))
    titlelabel.grid(column=1, row=0)

    temptitle = tkinter.Label(window, text="Temperature: ", font=("Ariel Bold", 15))
    temptitle.grid(column=0, row=2)

    phtitle = tkinter.Label(window, text="pH:", font=("Ariel Bold", 15))
    phtitle.grid(column=0, row=3)

    depthtitle = tkinter.Label(window, text="Depth: ", font=("Ariel Bold", 15))
    depthtitle.grid(column=0, row=4)

    distancetitle = tkinter.Label(window, text="Distance: ", font=("Ariel Bold", 15))
    distancetitle.grid(column=0, row=5)

    img = ImageTk.PhotoImage(Image.open("/home/chris/Documents/novid.png").resize((400, 400), Image.ANTIALIAS))
    vid1 = tkinter.Label(window, image=img)
    vid1.grid(column=0, row=6)

    img2 = ImageTk.PhotoImage(Image.open("/home/chris/Documents/novid.png").resize((400, 400), Image.ANTIALIAS))
    vid2 = tkinter.Label(window, image=img2)
    vid2.grid(column=1, row=6)

    roll = ImageTk.PhotoImage(Image.open("/home/chris/rov-side-image.png").resize((400, 400), Image.ANTIALIAS))
    l_roll = tkinter.Label(window, image=roll)
    l_roll.grid(column=0, row=7)

    pitch = ImageTk.PhotoImage(Image.open("/home/chris/rov_side_image.png").resize((400, 400), Image.ANTIALIAS))
    l_pitch = tkinter.Label(window, image=pitch)
    l_pitch.grid(column=1, row=7)


def start_line_track():
    pass


def measure_cannon():
    pass


def count_benthic():
    pass


def open_pid():
    t = tkinter.Toplevel()
    t.attributes('-type', 'dialog')
    t.wm_title("pee eye dees")
    l = tkinter.Label(t, text="do some tunin")
    l.grid(row=0, column=0)


def open_ssh():
    pass


def open_rov_mem():
    pass


def open_pc_mem():
    pass


def shutdown_rov():
    result = messagebox.askokcancel(":0", "Turn off ROV?")
    if result:
        if getpass.getuser() == "nugget":
            subprocess.call(['/home/nugget/surface/shutdown-rov.sh'])
        else:
            messagebox.showinfo(":)",
                                "The dashboard would have called the shutdown script, but you are not the Nugget user \
                                (dashboard does not believe you are on the surface station)")


def shutdown():
    result = messagebox.askokcancel(":0", "Turn off ROV and this PC?")
    if result:
        if getpass.getuser() == "nugget":
            subprocess.call(['/home/nugget/shutdown.sh'])
        else:
            messagebox.showinfo(":)",
                                "The dashboard would have called the shutdown script, but you are not the Nugget user \
                                (dashboard does not believe you are on the surface station)")


class dataframe_update(threading.Thread):
    def __init__(self, tk_root):
        self.root = tk_root
        self.joystick = None
        self.CONTENT_FONT_SIZE = 10

        threading.Thread.__init__(self)
        self.start()

    def update_ph(self, ph):
        if ph != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=1)
        return 1

    def update_ir(self, ir):
        if ir != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=2)
        return 1

    def update_depth(self, depth):
        if depth != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=3)
        return 1

    def update_temp(self, temp):
        if temp != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=4)
        return 1

    def update_t1(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=7)
        return 1

    def update_t2(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=8)
        return 1

    def update_t3(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=9)
        return 1

    def update_t4(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=10)
        return 1

    def update_t5(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=11)
        return 1

    def update_t6(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=12)
        return 1

    def update_t7(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=13)
        return 1

    def update_t8(self, t):
        if t != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=14)
        return 1

    def update_manip(self, m):
        if m != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=15)
        return 1

    def update_dumper(self, m):
        if m != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=16)
        return 1

    def update_probe(self, m):
        if m != 1:
            tkinter.Label(self.root, text="NYI", font=("Roboto", self.CONTENT_FONT_SIZE)).grid(column=1, row=17)
        return 1

    def update_ah(self, t):
        new = self.joystick.get_axis(0)
        if t != new:
            tkinter.Label(self.root, text="{:.2f}".format(new), font=("Roboto",
                                                                      self.CONTENT_FONT_SIZE)).grid(column=1, row=21)
        return new

    def update_av(self, t):
        new = self.joystick.get_axis(1)
        if t != new:
            tkinter.Label(self.root, text="{:.2f}".format(new), font=("Roboto",
                                                                      self.CONTENT_FONT_SIZE)).grid(column=1, row=22)
        return new

    def update_at(self, t):
        new = self.joystick.get_axis(2)
        if t != new:
            tkinter.Label(self.root, text="{:.2f}".format(new), font=("Roboto",
                                                                      self.CONTENT_FONT_SIZE)).grid(column=1, row=23)
        return new

    def update_al(self, t):
        new = self.joystick.get_axis(3)
        if t != new:
            tkinter.Label(self.root, text="{:.2f}".format(new), font=("Roboto",
                                                                      self.CONTENT_FONT_SIZE)).grid(column=1, row=24)
        return new

    def update_b1(self, b):
        new = self.joystick.get_button(0)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=26)
        return new

    def update_b2(self, b):
        new = self.joystick.get_button(1)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=27)
        return new

    def update_b3(self, b):
        new = self.joystick.get_button(2)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=28)
        return new

    def update_b4(self, b):
        new = self.joystick.get_button(3)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=29)
        return new

    def update_b5(self, b):
        new = self.joystick.get_button(4)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=30)
        return new

    def update_b6(self, b):
        new = self.joystick.get_button(5)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=31)
        return new

    def update_b7(self, b):
        new = self.joystick.get_button(6)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=32)
        return new

    def update_b8(self, b):
        new = self.joystick.get_button(7)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=33)
        return new

    def update_b9(self, b):
        new = self.joystick.get_button(8)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=34)
        return new

    def update_b10(self, b):
        new = self.joystick.get_button(9)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=35)
        return new

    def update_b11(self, b):
        new = self.joystick.get_button(10)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=36)
        return new

    def update_b12(self, b):
        new = self.joystick.get_button(11)
        if b != new:
            tkinter.Label(self.root, text=("1" if new else "0"), font=("Roboto",
                                                                       self.CONTENT_FONT_SIZE)).grid(column=1, row=37)
        return new

    def run(self):
        self.joystick = setup_joystick()
        # window = self.root

        ph = -1; ir = -1;  depth = -1; temp = -1; t1 = -1; t2 = -1; t3 = -1; t4= -1;
        t5 = -1; t6 = -1;     t7 = -1; t8 = -1; manip = -1; dumper = -1; probe = -1;
        ah = -1; av = -1;     at = -1; al = -1; b1 = -1; b2 = -1; b3 = -1; b4 = -1;
        b5 = -1; b6 = -1;     b7 = -1; b8 = -1; b9 = -1; b10 = -1; b11 = -1; b12 = -1

        while True:
            pygame.event.get()

            ph = self.update_ph(ph)
            ir = self.update_ir(ir)
            depth = self.update_depth(depth)
            temp = self.update_temp(temp)
            t1 = self.update_t1(t1)
            t2 = self.update_t2(t2)
            t3 = self.update_t3(t3)
            t4 = self.update_t4(t4)
            t5 = self.update_t5(t5)
            t6 = self.update_t6(t6)
            t7 = self.update_t7(t7)
            t8 = self.update_t8(t8)
            manip = self.update_manip(manip)
            dumper = self.update_dumper(dumper)
            probe = self.update_probe(probe)
            ah = self.update_ah(ah)
            av = self.update_av(av)
            at = self.update_at(at)
            al = self.update_al(al)
            b1 = self.update_b1(b1)
            b2 = self.update_b2(b2)
            b3 = self.update_b3(b3)
            b4 = self.update_b4(b4)
            b5 = self.update_b5(b5)
            b6 = self.update_b6(b6)
            b7 = self.update_b7(b7)
            b8 = self.update_b8(b8)
            b9 = self.update_b9(b9)
            b10 = self.update_b10(b10)
            b11 = self.update_b11(b11)
            b12 = self.update_b12(b12)

            sleep(0.01)
