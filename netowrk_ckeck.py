import socket

try:
	socket.gethostbyname("www.google.com")
except:
	print("No network")
		
