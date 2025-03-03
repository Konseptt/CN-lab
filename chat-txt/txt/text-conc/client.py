import socket

# Server connection details
HOST = '192.168.56.1'  # Change this to match the server
PORT = 57  # Updated port

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Get file name from user and send request to server
file_request = input("Enter the file name to request from the server: ")
client_socket.send(file_request.encode())

# Receive server's response about file existence
response = client_socket.recv(2)  # Check if file exists
if response == b"OK":
    # If file exists, receive and save it
    with open("received_" + file_request, "wb") as file:
        while chunk := client_socket.recv(4096):  # Receive file in chunks of 4KB
            if not chunk:
                break
            file.write(chunk)
    print(f"File received and saved as 'received_{file_request}'")
else:
    print("Error: File not found on server.")

# Clean up and close connection
client_socket.close()
print("Connection closed.")
