import socket
import os

# Define server IP and port
HOST = '192.168.56.1'  # Change to your local IP if needed
PORT = 59  # Use UDP Port 59

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP Server listening on {HOST}:{PORT}")

while True:
    # Receive file request from client
    file_request, client_address = server_socket.recvfrom(1024)
    file_request = file_request.decode()
    print(f"File request '{file_request}' from {client_address}")

    if os.path.exists(file_request):
        server_socket.sendto(b"OK", client_address)  # Confirm file exists
        with open(file_request, "rb") as file:
            while chunk := file.read(4096):  # Read in chunks
                server_socket.sendto(chunk, client_address)  # Send data
        server_socket.sendto(b"EOF", client_address)  # Indicate end of file transmission
        print(f"File '{file_request}' sent successfully to {client_address}")
    else:
        server_socket.sendto(b"ERROR: File not found", client_address)  # Send error

    print(f"Waiting for the next client request...\n")
