import socket

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('localhost', 12345))
message = "Привет, сервер!"
client1.send(message.encode())
print(client1.recv(1024).decode())
client1.close()

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect(('localhost', 12345))
message = "Как дела?"
client2.send(message.encode())
print(client2.recv(1024).decode())
client2.close()
