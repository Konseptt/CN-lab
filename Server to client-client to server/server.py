import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

s.bind(('192.168.56.1', 8080))

s.listen(5)
print("Waiting for connection")



while True:
    conn, addr = s.accept()
    print("Connected with", addr)
    conn.send(bytes("Hi", 'utf-8'))
    
    client_message = conn.recv(1024).decode()  
    print("Client says:", client_message)
    conn.close()
