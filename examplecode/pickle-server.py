import socket, pickle, pygame, os, sys
joyvals = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

HOST = 'localhost'
PORT = 2017
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

pygame.joystick.init()
pygame.init()
try:
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
except pygame.error:
    os.execl(sys.executable, sys.executable, *sys.argv)

joystick.init()

def getbutton(index):
    returnbool = dict[index+4] != joystick.get_button(index)
    if returnbool:
        dict[index + 4] = joystick.get_button(index)
    return returnbool

b1 = -1; b2 = -1; b3 = -1; b4 = -1; b5 = -1; b6 = -1; b7 = -1;
b8 = -1; b9 = -1; b10 = -1; b11 = -1; b12 = -1; ha = -1;
va = -1; ta = -1; la = -1;

while True:
    isnew = False
    pygame.event.get()
    joyvals[0] = joystick.get_button(0)
    joyvals[1] = joystick.get_button(1)
    joyvals[2] = joystick.get_button(2)
    joyvals[3] = joystick.get_button(3)
    joyvals[4] = joystick.get_button(4)
    joyvals[5] = joystick.get_button(5)
    joyvals[6] = joystick.get_button(6)
    joyvals[7] = joystick.get_button(7)
    joyvals[8] = joystick.get_button(8)
    joyvals[9] = joystick.get_button(9)
    joyvals[10] = joystick.get_button(10)
    joyvals[11] = joystick.get_button(11)
    joyvals[12] = joystick.get_axis(0)
    joyvals[13] = joystick.get_axis(1)
    joyvals[14] = joystick.get_axis(2)
    joyvals[15] = joystick.get_axis(3)
    joyvals[16] = 0  # do line following
    joyvals[17] = 0  # do shutdown

    data = pickle.dumps(joyvals)
    s.send(data)
