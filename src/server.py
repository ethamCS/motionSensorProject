import socket

s = socket.socket()
print("Socket created successfully")

port = 12345

s.bind((socket.gethostname(), port))
print(f"Socket bound to {port}")

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print(f"Alert from {addr}")
    msg = "Alert Recieved\n"
    byt = msg.encode()
    c.send(byt)
    c.close()
