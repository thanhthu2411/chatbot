# Socket Chatbot

A chatbot built with Python sockets. A server listens for connections over TCP, and a client with a chat window (CustomTkinter) sends messages to it. The bot is rule-based: it understands simple prompts like greetings, the time, the weather for a city, and goodbye.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone or download this repository
2. Install the GUI library: `pip install customtkinter`
3. Start the server in one terminal: `python server.py` (it listens on `127.0.0.1`, port `7000`)
4. Start the client in a second terminal: `python client.py`

Note: the weather feature needs an internet connection. If you're offline, the bot replies with an error message instead.

Instructions for using the software:

1. Type a message in the box at the bottom of the chat window and press Enter or click Send
2. Try these prompts: `hello`, `what time is it?`, `weather in Boise`, `help`
3. Say `bye` or `goodbye` to end the chat. The client closes its connection and the input is disabled
4. To chat again, close the window and start `client.py` again. The server keeps running and waits for the next client

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3.8 or higher (check with `python --version`)
* `customtkinter` (installed with pip)
* `tkinter` (comes with Python on Windows and macOS; on some Linux systems you need to install it, for example `sudo apt install python3-tk`)
* Everything else (`socket`, `json`, `re`, `urllib`, `datetime`) is part of the Python standard library

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Socket Programming in Python (Real Python)](https://realpython.com/python-sockets/)
* [Python Socket Programming: Server and Client Guide (DigitalOcean)](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)
* [Python socket module documentation](https://docs.python.org/3/library/socket.html)
* [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/)
* [Open-Meteo Weather API](https://open-meteo.com/en/docs)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Handle multiple clients at the same time using threads
* [ ] Add message boundaries (for example, one message per line) so messages can't merge in the TCP stream
* [ ] Run the network calls in a background thread so the chat window doesn't freeze while waiting for a reply
* [ ] Add a web-based chat page
* [ ] Connect the chatbot to my marketplace app so it can answer questions about listings