# -*- coding:utf-8 -*-
import socket
import json

host = "127.0.0.1" #お使いのサーバーのホスト名を入れます
port = 5000 #クライアントと同じPORTをしてあげます

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします


print('Waiting for connections...')

#clientsock, client_address = serversock.accept() #接続されればデータを格納

while True:
    serversock.listen(10)
    clientsock, client_address = serversock.accept() #接続されればデータを格納
    print("flag")

    while True:

        rcvmsg = clientsock.recv(4096) #ここの時点でbytes


        rcvmsg = rcvmsg.decode('utf-8')
        #rcvmsg = rcvmsg.encode('utf-8')
        rcvmsg = json.loads(rcvmsg)
        print('Received -> ')
        print(rcvmsg)
        if rcvmsg == '':
            break

        print('Type message...')
        break
        #clientsock.close()


serversock.close()
