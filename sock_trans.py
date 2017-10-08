# -*- coding:utf-8 -*-
import socket
import json

host = "127.0.0.1" #お使いのサーバーのホスト名を入れます
port = 5000 #適当なPORTを指定してあげます

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

client.connect((host, port)) #これでサーバーに接続します

obj = {
"1":{
    "location":["0.2", "0.2", "0.8"],
    "motion":"POINTING",
    "name":"エルモ"
},
"2":{
    "location":["0.2", "0.2", "0.8"],
    "motion":"POINTING",
    "name":"エルモ"
},
"3":{
    "location":["0.2", "0.2", "0.8"],
    "motion":"POINTING",
    "name":"エルモ"
},
"4":{
    "location":["0.2", "0.2", "0.8"],
    "motion":"POINTING",
    "name":"エルモ"
},
"5":{
    "location":["0.2", "0.2", "0.8"],
    "motion":"POINTING",
    "name":"エルモ"
},
}

obj_sock = json.dumps(obj)


client.send(obj_sock.encode('utf-8')) #適当なデータを送信します（届く側にわかるように）


#response = client.recv(4096) #レシーブは適当な2進数にします（大きすぎるとダメ）
client.close()

#print(response)
