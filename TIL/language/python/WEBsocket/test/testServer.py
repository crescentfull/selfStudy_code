from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print("---------------------------")
print(str(addr),"에서 접속하였습니다.!")
print("---------------------------")

data = connectionSock.recv(1024)
print("받은 데이터 : ", data.decode('utf-8'))

connectionSock.send("서버 입니다.".encode('utf-8'))
print("SEND MESSAGE")