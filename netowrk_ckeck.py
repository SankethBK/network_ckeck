import socket

print("Cheking your network")
def network_check():
	try:
		socket.gethostbyname("www.google.com")
	except:
		print("No network")
			
network_check()

