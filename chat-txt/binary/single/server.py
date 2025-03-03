import socket

# Define server IP and port
HOST = '192.168.56.1'
PORT = 56

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Allow up to 5 clients to wait in queue
print(f"Server listening on {HOST}:{PORT}")

while True:
    print("Waiting for a client connection...")
    conn, addr = server_socket.accept()
    print(f"Connected with {addr}")
    
    # Receive file request from client
    file_request = conn.recv(1024).decode()

    try:
        with open(file_request, 'rb') as file:
            while chunk := file.read(4096):  # Read in chunks
                conn.sendall(chunk)  # Send raw bytes
        print("File sent successfully")
    except FileNotFoundError:
        conn.sendall(b"ERROR: File not found")  # Send raw error message
    
    conn.close()
    print("Client disconnected. Waiting for the next client...")
