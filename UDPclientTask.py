from socket import *
import sys
y = sys.argv[1]
x=sys.argv[2]
serverIP = '127.0.0.1'
serverPort = 12000
client_port=int(y)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('',client_port))
message = str(x)
clientSocket.sendto(message.encode(),(serverIP,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print ((modifiedMessage.decode()))
clientSocket.close()