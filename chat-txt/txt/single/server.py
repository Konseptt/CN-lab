import socket
import os

# Server configuration
HOST = '192.168.56.1'  # Change to your local IP if needed
PORT = 55  # Port for single client connection

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Listen for single client

print(f"Server listening on {HOST}:{PORT}")

# Main server loop - handles one client and exits
while True:
    # Accept incoming connection
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    # Receive file request from client
    file_request = conn.recv(1024).decode()

    # Check if requested file exists and send it
    if os.path.exists(file_request):
        conn.sendall(b"OK")  # Signal file found
        with open(file_request, "rb") as file:
            while chunk := file.read(4096):  # Read file in 4KB chunks
                conn.sendall(chunk)
        print("File sent successfully.")
    else:
        conn.sendall(b"ERROR")  # Signal file not found

    # Clean up connection
    conn.close()
    print("Connection closed.")
    break  # Exit after serving one client
