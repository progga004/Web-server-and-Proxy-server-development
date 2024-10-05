from socket import *
import os

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

def serve_file(file_path, connectionSocket):
    if file_path.endswith(".html") or file_path.endswith(".txt"):
        content_type = "text/html" if file_path.endswith(".html") else "text/plain"
        with open(file_path, 'r') as file:
            content = file.read()
            header = f"HTTP/1.1 200 OK\nContent-Type: {content_type}\n\n"
            connectionSocket.send(header.encode() + content.encode())
    else:
        content_type = "image/jpeg" if file_path.endswith(".jpg") or file_path.endswith(".jpeg") else "image/png"
        with open(file_path, 'rb') as file:
            content = file.read()
            header = f"HTTP/1.1 200 OK\nContent-Type: {content_type}\n\n"
            connectionSocket.send(header.encode() + content)

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        file_path = message.split()[1]
        if file_path.startswith('/'):
            file_path = file_path[1:]
        if file_path == "":
            file_path = "index.html"  

        if os.path.isfile(file_path):
            serve_file(file_path, connectionSocket)
        else:
            header = "HTTP/1.1 404 Not Found\n\n"
            content = "<html><body><h1>404 Not Found</h1></body></html>"
            connectionSocket.send((header + content).encode())

    except IndexError:
        header = "HTTP/1.1 400 Bad Request\n\n"
        content = "<html><body><h1>400 Bad Request</h1></body></html>"
        connectionSocket.send((header + content).encode())
    finally:
        connectionSocket.close()
