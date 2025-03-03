import socket

# Server connection configuration
HOST = '192.168.56.1'  # Server IP address
PORT = 55  # Server port number

# Initialize client socket and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Get file name from user and send request
file_request = input("Enter the file name to request from the server: ")
client_socket.send(file_request.encode())

# Handle server response
response = client_socket.recv(2)  # Get initial response (OK/ERROR)
if response == b"OK":
    # Receive and save file
    with open("received_" + file_request, "wb") as file:
        while chunk := client_socket.recv(4096):  # Receive in 4KB chunks
            file.write(chunk)
    print(f"File received and saved as 'received_{file_request}'")
else:
    print("Error: File not found on server.")

# Clean up
client_socket.close()
print("Connection closed.")
