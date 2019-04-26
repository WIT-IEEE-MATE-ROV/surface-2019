import socket, pickle, pygame, os, sys
from time import sleep
from tkinter import messagebox

HOST = 'nugpotpi.local'
PORT = 2015
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
except:
    s = None
    print("Socket failed")
#    result = messagebox.askokcancel("YOU'RE NOT CONNECTED STOOPID", "Socket "+
#                           "connection failed, hit OK to restart and try "+
#                           "connecting again or hit cancel to proceed without a "+
#                           "connection. (Nothing will happen on the ROV, but this "+
#                           "might be useful for debug)")
#    if result:
#        os.execl(sys.executable, sys.executable, *sys.argv)

arr = ([1,2,3,4], [1,2,3,4,5,6,7,8,9,10,11,12], [1], [1,2])
old = ([1,2,3,4], [1,2,3,4,5,6,7,8,9,10,11,12], [1], [1,2])


def hattoval(a, b):
    if a == 0:
        if b == 0:
            return 0
        if b == 1:
            return 1
        if b == -1:
            return 5
    if a == 1:
        if b == 0:
            return 3
        if b == 1:
            return 2
        if b == -1:
            return 4
    if a == -1:
        if b == 0:
            return 7
        if b == 1:
            return 8
        if b == -1:
            return 6


pygame.joystick.init()
pygame.init()
try:
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
except pygame.error:
    print("pygame error")
    os.execl(sys.executable, sys.executable, *sys.argv)

joystick.init()

while True:
    try:
        # old = deepcopy(arr)
        pygame.event.get()

        hat = joystick.get_hat(0)
        arr[2][0] = hattoval(hat[0], hat[1])

        arr[0][0] = joystick.get_axis(0)
        arr[0][1] = joystick.get_axis(1)
        arr[0][2] = joystick.get_axis(2)
        arr[0][3] = joystick.get_axis(3)

        arr[1][0] = joystick.get_button(0)
        arr[1][1] = joystick.get_button(1)
        arr[1][2] = joystick.get_button(2)
        arr[1][3] = joystick.get_button(3)
        arr[1][4] = joystick.get_button(4)
        arr[1][5] = joystick.get_button(5)
        arr[1][6] = joystick.get_button(6)
        arr[1][7] = joystick.get_button(7)
        arr[1][8] = joystick.get_button(8)
        arr[1][9] = joystick.get_button(9)
        arr[1][10] = joystick.get_button(10)
        arr[1][11] = joystick.get_button(11)

        data_string = pickle.dumps(arr)
        if s is not None:
            s.send(data_string)
            data = s.recv(4096)
        # data_arr = pickle.loads(data)
        print(arr)
        sleep(.01)

    except KeyboardInterrupt:
        s.send("Keyboard interrupt-- Bye!".encode())
        if s is not None:
            s.close()
        sys.exit()
