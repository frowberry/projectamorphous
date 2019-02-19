import socket

def main():
	host = input("Please input your local ip address: ")
	port = 5000

	s = socket.socket()
	s.bind((host, port))



	s.listen(1)
	c, addr = s.accept()
	c.send(b'This is the Question Master')
	print("Connection from: ", str(addr))
	while True:
		data = c.recv(1024).decode('utf-8')
		if not data:
			break
		print("from connected user: ", str(data))
		data = input("What would you like to reply? ")
		print("sending...")
		c.send(data.encode('utf-8'))
		print("sent")
	c.close()

if __name__ == '__main__':
	main()
