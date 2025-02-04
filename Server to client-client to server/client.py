import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('192.168.56.1', 8080))

server_message = c.recv(1024).decode() 
print("Server says:", server_message)
c.send(bytes("Hi", 'utf-8'))
c.close()
