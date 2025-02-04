import socket

# Define the server IP and port
HOST = '192.168.56.1'
PORT = 55

# Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect the client to the server's IP and port
    client_socket.connect((HOST, PORT))
    print(f"Connected to the server at {HOST} on port {PORT}")

    # Request a file from the server
    file_request = input("Enter the name of the file to request from the server: ")
    client_socket.send(bytes(file_request, 'utf-8'))

    # Receive the file content from the server
    file_data = client_socket.recv(4096).decode()
    print("\nReceived from server:")
    print(file_data)
finally:
    # Close the connection
    client_socket.close()
    print("Connection closed")
