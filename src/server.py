import socket

s = socket.socket()
print("Socket created successfully")

port = 12345

s.bind(('', port))
print(f"Socket binded to {port}")

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print(f"Got connection from {addr}")
    msg = "Hello client!\n"
    byt = msg.encode()
    c.send(byt)
    c.close()
