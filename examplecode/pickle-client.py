import socket, pickle, sys

HOST = 'localhost'
PORT = 2017
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    try:
        data = s.recv(4096)
        data_arr = pickle.loads(data)
        print(repr(data_arr))
    except KeyboardInterrupt:
        s.close()
        sys.exit()
