import socket

def network_check():
	try:
		socket.gethostbyname("www.google.com")
	except:
		print("No network")
network_check()
			
