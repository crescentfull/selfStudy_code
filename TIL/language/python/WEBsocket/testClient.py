from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print("CONNENCTION SUCCESS")
clientSock.send("클라이언트 입니다.".encode('utf-8'))

print("SEND MESSAGE")

data = clientSock.recv(1024)
print("받은 데이터 : ", data.decode('utf-8'))
