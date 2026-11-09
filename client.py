import socket
from brain import is_goodbye
import customtkinter as ctk

HOST = "127.0.0.1"
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
print("Connected to server. Type 'quit' to exit.")

# while True:
#     text =  input("You: ").strip().lower()
    
#     if text == "":
#         continue
    
#     client.sendall(text.encode())
    
#     reply = client.recv(1024)
#     print("Server:", reply.decode())

#     if is_goodbye(text):
#         break

# client.close()

window = ctk.CTk()
window.title("Chatbot")
window.geometry("800x600")

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

chat_box = ctk.CTkScrollableFrame(window, width=700, height=450)
chat_box.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="")
chat_box.grid_columnconfigure(0, weight=1)
chat_box.grid_rowconfigure(0, weight=1)

input_row = ctk.CTkFrame(window, fg_color="transparent")
input_row.grid(row=1, column=0, padx=10, pady=(5, 40), sticky="")
input_row.grid_columnconfigure(0, weight=1)    

entry = ctk.CTkEntry(input_row, placeholder_text="Type a message...", width=450, height=40)
entry.grid(row=0, column=0, padx=(0, 5), sticky="ew")

send_button = ctk.CTkButton(input_row, text="Send", width=70)
send_button.grid(row=0, column=1)



window.mainloop()    
