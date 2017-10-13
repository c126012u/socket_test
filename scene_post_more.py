# -*- coding:utf-8 -*-
import socket
import json
import sys
import time

host = "127.0.0.1" #お使いのサーバーのホスト名を入れます
port = 5000 #適当なPORTを指定してあげます

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

global i
#i=0
client.connect((host, port)) #これでサーバーに接続します
#while True:

i = sys.stdin.readline()
with open("data1/data1-"+i[0:-1]+".json") as f:
    obj = json.load(f)
obj_sock = json.dumps(obj)


client.send(obj_sock.encode('utf-8')) #適当なデータを送信します（届く側にわかるように）
#i=i+1
print(i)

#time.sleep(1)

client.close()

#if int(i[0:-1])>50:
#    break

#data = sys.stdin.readline()
'''
if data == "data1\n":
    with open("data1/data1.json") as f:
        obj = json.load(f)
elif data == "data2\n":
    with open("data2/data2.json") as f:
        obj = json.load(f)
elif data == "data3\n":
    with open("data3/data3.json") as f:
        obj = json.load(f)
'''
