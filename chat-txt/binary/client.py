import socket

# Define server IP and port
HOST = '192.168.56.1'
PORT = 56

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"Connected to the server at {HOST} on port {PORT}")

# Request a file from the server
file_request = input("Enter the name of the file to request from the server: ")
client_socket.send(file_request.encode())  # Send filename as request

# Open a file to save raw bytes
with open(f"received_{file_request}", 'wb') as file:
    while True:
        file_data = client_socket.recv(4096)
        if not file_data:
            break  # Stop receiving when no more data
        file.write(file_data)  # Write raw bytes to file

print(f"File received and saved as received_{file_request}")

# Close the connection
client_socket.close()
print("Connection closed")
