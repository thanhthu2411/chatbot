import socket
from brain import is_goodbye

HOST = "127.0.0.1"
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
print("Connected to server. Type 'quit' to exit.")

while True:
    text =  input("You: ").strip().lower()
    
    if text == "":
        continue
    
    client.sendall(text.encode())
    
    reply = client.recv(1024)
    print("Server:", reply.decode())

    if is_goodbye(text):
        break

client.close()