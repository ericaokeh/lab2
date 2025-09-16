import socket

host = "127.0.0.1"  
port = 5000        


srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((host, port))
srv.listen(1)

print("Server is running on", host, "port", port)
print("Waiting for a client...")

conn, addr = srv.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    msg = data.decode().strip()
    print("Client:", msg)

    if msg.lower() == "quit":
        conn.send("Goodbye\n".encode())
        break

    reply = "You said: " + msg + "\n"
    conn.send(reply.encode())

conn.close()
srv.close()
