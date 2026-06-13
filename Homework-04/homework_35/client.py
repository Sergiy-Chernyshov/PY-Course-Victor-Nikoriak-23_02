import socket


HOST = "127.0.0.1"
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    message = "Hello, multiprocessing server!"
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)

print("Received from server:", data.decode())