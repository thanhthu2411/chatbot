import socket
import time
import brain

HOST = "127.0.0.1"
PORT = 7000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen()
print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"Client connected: {addr}")
    
    with conn:
        while True:
            data = conn.recv(1024)
            
            if not data:
                break
            
            message = data.decode()
            print("Received:", message)
            
            reply = brain.reply(message)
            conn.sendall(reply.encode())
            
        print("Client disconnected")