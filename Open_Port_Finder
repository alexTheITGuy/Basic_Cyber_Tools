import socket

#AF_INET refers to IPv4 while SOCK_STREAM refers to TCP connection-oriented protocol
#Creates a socket
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err))

#Define server or host to connect to as well as the specific port
hostName = input("Enter Host Name: ")
port = int(input("Enter a Port to Scan: "))


#Resolves the host name to a specific IPv4
try: 
    host_ip = socket.gethostbyname(hostName) 
except socket.gaierror: 
     print ("there was an error resolving the host")
     sys.exit() 

#Creates the connection if pissible 
s.connect((host_ip, port)) 
print ("the socket has successfully connected to", hostName)
s.shutdown(socket.SHUT_RDWR)
s.close()
