import socket

s = socket.socket()
print("socket successfully created")

port = 40674

s.bind(('',port))
print("socket binded successfully to %s"%(port))

s.listen(5)
print("socket is listening")

while True:
	c, addr = s.accept()
	print("got connection from",addr)
	#converts string to bye by using the 'b' before string
	c.send(b"thank you for connecting")
	
	c.close()