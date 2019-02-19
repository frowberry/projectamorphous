import socket

def main():
	host = '10.144.37.139'
	port = 5000

	s = socket.socket()
	s.bind((host, port))

	print("awaiting for connection...")
	s.listen(1)
	c, addr = s.accept()
	print("Connection from: ", str(addr))
	while True:
		data = c.recv(1024).decode('utf-8')
		if not data:
			break
		data = data.upper()
		c.send(data.encode('utf-8'))
	c.close()

if __name__ == '__main__':
	main()
