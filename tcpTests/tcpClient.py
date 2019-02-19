import socket

def main():
	host = "10.144.37.139"
	port = 5000

	s = socket.socket()
	s.connect((host,port))
	print("Recieved from server: ", s.recv(1024).decode('utf-8'))
	message = input("-> ")
	while message != 'q':
		s.send(message.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		print ("Recieved from server: ", str(data))
		message = input("-> ")
	s.close()

