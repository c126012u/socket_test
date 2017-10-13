# -*- coding:utf-8 -*-
import socket
import json
import sys

host = "127.0.0.1" #お使いのサーバーのホスト名を入れます
port = 5000 #適当なPORTを指定してあげます

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

client.connect((host, port)) #これでサーバーに接続します

print("data1:API用")
print("data2:「これ好き？」")
print("data3:「りんごありますか？」")


data = sys.stdin.readline()

if data == "data1\n":
    with open("data1/api.json") as f:
        obj = json.load(f)
elif data == "data2\n":
    with open("data2/koresuki.json") as f:
        obj = json.load(f)
elif data == "data3\n":
    with open("data3/ringoari.json") as f:
        obj = json.load(f)


obj_sock = json.dumps(obj)


client.send(obj_sock.encode('utf-8')) #適当なデータを送信します（届く側にわかるように）

client.close()
