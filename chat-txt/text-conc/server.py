import socket
import os
import threading

HOST = '192.168.56.1'  # Change to your local IP if needed
PORT = 57  # Updated port

# Function to handle a client connection
def handle_client(conn, addr):
    print(f"Connected to {addr}")

    file_request = conn.recv(1024).decode()

    if os.path.exists(file_request):
        conn.sendall(b"OK")  # Indicate file exists
        with open(file_request, "rb") as file:
            while chunk := file.read(4096):  # Read and send in chunks
                conn.sendall(chunk)
        print(f"File '{file_request}' sent successfully to {addr}.")
    else:
        conn.sendall(b"ERROR")  # Indicate file not found

    conn.close()
    print(f"Connection with {addr} closed.")

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Allow multiple clients to connect
print(f"Server listening on {HOST}:{PORT}")

# Accept multiple clients using threading
while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
