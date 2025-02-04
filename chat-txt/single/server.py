# server.py
import socket

# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# Bind the socket to the specific IP address and port 55
server_socket.bind(('192.168.56.1', 55))
print("Socket bound to IP 192.168.56.1 and port 55")

# Start listening for incoming connections, with a maximum queue of 5
server_socket.listen(5)
print("Waiting for connection")

# Accept a connection from a client
conn, addr = server_socket.accept()
print("Connected with", addr)

# Receive the client's request for a file
client_message = conn.recv(1024).decode()
print("Client requested:", client_message)

try:
    # Open and read the requested file
    with open(client_message, 'r') as file:
        file_data = file.read()

    # Send the file content to the client
    conn.send(bytes(file_data, 'utf-8'))
    print("File sent successfully")
except FileNotFoundError:
    # If the file is not found, send an error message
    error_message = "Error: File not found"
    conn.send(bytes(error_message, 'utf-8'))
    print("File not found error sent to client")

# Close the connection
conn.close()
server_socket.close()
print("Connection closed")