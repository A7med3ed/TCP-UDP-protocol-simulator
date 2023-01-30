from socket import *
serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
while True:
 sentence = input('Enter message to send or type Exit to disconnect: ')
 clientSocket.send(sentence.encode())
 the_replay = clientSocket.recv(1024).decode()
 print("Received Message from server:", the_replay)
 if(the_replay=="Disconnect"):
  print("Now you are Disconnected from server")
  clientSocket.close()
  exit()