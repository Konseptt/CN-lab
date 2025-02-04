import socket
import threading

# Define the server IP and port
HOST = '192.168.56.1'
PORT = 55

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected with {addr}")
    try:
        # Receive the client's request for a file
        client_message = conn.recv(1024).decode()
        print(f"Client {addr} requested: {client_message}")

        try:
            # Open and read the requested file
            with open(client_message, 'r') as file:
                file_data = file.read()

            # Send the file content to the client
            conn.send(bytes(file_data, 'utf-8'))
            print(f"File '{client_message}' sent to {addr}")
        except FileNotFoundError:
            # If the file is not found, send an error message
            error_message = "Error: File not found"
            conn.send(bytes(error_message, 'utf-8'))
            print(f"File '{client_message}' not found, error sent to {addr}")
    finally:
        # Close the connection
        conn.close()
        print(f"Connection with {addr} closed")

# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}")

# Accept multiple clients
while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
