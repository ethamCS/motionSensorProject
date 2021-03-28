import socket

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

while True:
    byt = s.recv(4096)
    msg = byt.decode()
    last_msg = ""
    if (last_msg != msg):
        print(msg)
        last_msg = msg

s.close()
