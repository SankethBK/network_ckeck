import socket
print("Cheking your network")
try:
	socket.gethostbyname("www.google.com")
except:
	print("No network")
		
