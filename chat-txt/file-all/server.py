import socket
import os

HOST = '192.168.56.1'  # Change to your local IP if needed
PORT = 55

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    file_request = conn.recv(1024).decode()

    if os.path.exists(file_request):
        conn.sendall(b"OK")  # Indicate file exists
        with open(file_request, "rb") as file:
            while chunk := file.read(4096):  # Read and send in chunks
                conn.sendall(chunk)
        print("File sent successfully.")
    else:
        conn.sendall(b"ERROR")  # Indicate file not found

    conn.close()
    print("Connection closed.")
    break
