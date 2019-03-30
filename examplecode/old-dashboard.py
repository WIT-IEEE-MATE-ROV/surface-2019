import tkinter
import threading
import dashboardutils as dbu
from time import sleep
from PIL import Image, ImageTk

window = tkinter.Tk()
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

joystick = dbu.setup_joystick()

class App(threading.Thread):
    def __init__(self, tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        h = -1; v = -1; t = -1; l = -1; temp = -1; ph = -1; depth = -1; dist = -1

        while True:
            p_h = h; p_v = v; p_t = t; p_l = l
            h, v, t, l = dbu.getaxis(joystick)
            if h != p_h or v != p_v or t != p_t or p_l != l:
                joylabel = tkinter.Label(window,
                                         text="X: {:.3f} Y: {:.3f} C: {:.3f} L: {:.3f}".format(h-1, v-1, t-1, l-1),
                                         font=("Ariel Bold", 15))
                joylabel.grid(column=1, row=1)

            p_temp = temp
            temp = dbu.gettemp()
            if p_temp != temp:
                templabel = tkinter.Label(window, text="{:s}".format(temp),
                                          font=("Ariel Bold", 15))
                templabel.grid(column=1, row=2)

            p_ph = ph
            ph = dbu.getph()
            if p_ph != ph:
                phlabel = tkinter.Label(window, text="{:s}".format(ph),
                                        font=("Ariel Bold", 15))
                phlabel.grid(column=1, row=3)

            p_depth = depth
            depth = dbu.getdepth()
            if p_depth != depth:
                depthlabel = tkinter.Label(window, text="{:s}".format(depth),
                                           font=("Ariel Bold", 15))
                depthlabel.grid(column=1, row=4)

            p_dist = dist
            dist = dbu.getdist()
            if p_dist != dist:
                distlabel = tkinter.Label(window, text="{:s}".format(depth),
                                          font=("Ariel Bold", 15))
                distlabel.grid(column=1, row=5)

            sleep(0.01)


app = App(window)
window.mainloop()
