import socket
from brain import is_goodbye
import customtkinter as ctk

HOST = "127.0.0.1"
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# while True:
#     text =  input("You: ").strip().lower()
    
#     if text == "":
#         continue
    
#     client.sendall(text.encode())
    
#     reply = client.recv(1024)
#     print("Server:", reply.decode())

#     if is_goodbye(text):
#         break

chat_over = False

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

def add_message(text, sender):
    mes_label = ctk.CTkLabel(chat_box, text=text, wraplength=260, justify="left",
                             fg_color="darkblue", text_color="white", corner_radius=10)
    if sender == "client":
        mes_label.pack(anchor="e", padx=5, pady=10, ipadx=5, ipady=5)
    else:
        mes_label.pack(anchor="w", padx=5, pady=10, ipadx=5, ipady=5)



try:
    client.connect((HOST, PORT))
    print("Connected to server. Type 'quit' to exit.")

except OSError:         
    add_message("Can't reach the server. Is server.py running?", "server")
    entry.configure(state="disabled")
    send_button.configure(state="disabled")


def send_message(event=None):
    if chat_over:                      
        return
    
    text = entry.get().strip()
    
    if not text:
        return
    
    entry.delete(0, "end")
    
    add_message(text, "client")
    window.update_idletasks()
    
    try:
        client.sendall(text.encode())
        reply = client.recv(1024)
    except OSError:      
        add_message("Lost connection to the server.", "server")
        end_chat()
        return
    
    
    if not reply:                     
        add_message("The server closed the connection.", "server")
        end_chat()
        return
    
    add_message(reply.decode(), "server")
    
    if is_goodbye(text):
        end_chat()

def end_chat():
    global chat_over
    chat_over = True
    entry.configure(state="disabled")
    send_button.configure(state="disabled")
    client.close()

def on_close():
    client.close()
    window.destroy()  


send_button.configure(command=send_message)
entry.bind("<Return>", send_message)
window.protocol("WM_DELETE_WINDOW", on_close)


window.mainloop()    
