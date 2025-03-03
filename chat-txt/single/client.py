import socket

HOST = '192.168.56.1'  # Change this to match the server
PORT = 55

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

file_request = input("Enter the file name to request from the server: ")
client_socket.send(file_request.encode())

response = client_socket.recv(2)  # Check if file exists
if response == b"OK":
    with open("received_" + file_request, "wb") as file:
        while chunk := client_socket.recv(4096):
            file.write(chunk)
    print(f"File received and saved as 'received_{file_request}'")
else:
    print("Error: File not found on server.")

client_socket.close()
print("Connection closed.")
