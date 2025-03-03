import socket

# Define server IP and port
HOST = '192.168.56.1'  # Change this to match the server
PORT = 59  # Use UDP Port 59

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Request a file from the server
file_request = input("Enter the name of the file to request from the server: ")
client_socket.sendto(file_request.encode(), (HOST, PORT))  # Send filename as request

# Receive server response
response, _ = client_socket.recvfrom(1024)

if response == b"OK":
    with open(f"received_{file_request}", "wb") as file:
        while True:
            file_data, _ = client_socket.recvfrom(4096)
            if file_data == b"EOF":
                break  # Stop receiving when EOF is received
            file.write(file_data)  # Write raw bytes to file
    
    print(f"File received and saved as 'received_{file_request}'")

else:
    print(response.decode())  # Print error message if file not found

# Close the socket immediately after receiving the file
client_socket.close()
print("Connection closed.")
