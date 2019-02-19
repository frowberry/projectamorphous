import socket

host = input("please input ip")
port = 5000

s = socket.socket()
s.connect((host, port))

message = input("-> ")
while message != 'q':
	s.send(message.encode('utf-8'))
	data = s.recv(1024).decode('utf-8')
	print("Received from server: ", str(data))
	message = input("-> ")
s.close()

