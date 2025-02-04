import socket

# Create a socket object
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to localhost (127.0.0.1) instead of 0.0.0.0
c.connect(('127.0.0.1', 8080))  # or 'localhost' instead of 127.0.0.1

server_message = c.recv(1024).decode() 
print("Server says:", server_message)
c.send(bytes("Hi", 'utf-8'))
c.close()