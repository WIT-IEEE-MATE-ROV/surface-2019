import socket, pickle

HOST = 'localhost'
PORT = 2013
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(4096)
    if not data: break
    fromsurface = pickle.loads(data)
    conn.send(data)
conn.close()