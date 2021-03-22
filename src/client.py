import socket

socket = socket.socket()

port = 12345

socket.connect(('10.0.0.3', port))

byt = socket.recv(4096)
msg = byt.decode()
print(msg)

socket.close
