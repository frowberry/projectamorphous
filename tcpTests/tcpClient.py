import socket

def main():
	host = input("please input the ip address you would like to connect to: ")
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

if __name__ == '__main__':
	main()