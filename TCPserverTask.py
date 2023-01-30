from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("listening at:""("+"'0.0.0.0'"+" , "+"1060"+")")
connectionSocket, addr = serverSocket.accept()
print("The server connect to:",addr)
print("socket connects between","("+"'127.0.0.1'"+" , "+"1060"+")","and",addr)
while True:
  

  sentence = connectionSocket.recv(1024).decode()
  print("Resived message from client:",sentence)
  if(sentence=="Exit"):
   print("Replay sent,server socket closed")
   exit_message="Disconnect"
   connectionSocket.send(exit_message.encode())
   connectionSocket.close()
   print("listening at:""("+"'0.0.0.0'"+" , "+"1060"+")")
   exit()
   
  size=("Your data was"+" "+str(int((len(sentence.encode('utf-16-le')))/2))+" "+"bytes")
  connectionSocket.send(size .encode())
