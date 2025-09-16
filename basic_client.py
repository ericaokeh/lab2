import socket

host = "127.0.0.1"
port = 5000

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((host, port))

print("Connected to server. Type 'quit' to exit.")

# chat loop
while True:
    text = input("You: ")
    cli.send((text + "\n").encode())

    data = cli.recv(1024)
    if not data:
        print("Server closed connection.")
        break

    reply = data.decode().strip()
    print("Server:", reply)

    if text.lower() == "quit":
        break

cli.close()
