#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jtalk #OpenJTalk
import talk #talkAPI
from rule_base import res7
import socket
import time
import sys
import threading

recv_data = {}
class chat(threading.Thread):

	def __init__(self):
		super(chat, self).__init__()
		self.setDaemon(True)


	def run(self):
		while True:
			print("認識開始：Enter")
			trig = sys.stdin.readline()
			speech = {'sentence1': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence2': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence3': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence4': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence5': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence6': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence7': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence8': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence9': {'sentence': '', 'score': '0', 'word': [], 'CM': []}, 'sentence10': {'sentence': '', 'score': '0', 'word': [], 'CM': []}}

			scene = {'':{'location':[],'motion':'','name':[],'confidence':[]} }
			if "sentence1" in recv_data:
				speech = recv_data
			elif recv_data != {}:
				scene = recv_data

			while trig == "\n":
				while True:
					res = res7.main(speech, scene)
					if res == {}: #resの音声なしの時
						print("0.1秒待つ")
						time.sleep(5)
						print("終わり")
						break
					elif res["RESPONSE"]==res["ID"]==res["ORDER"]=="":
						res["RESPONSE"] = talk.chat(res["input_txt"])


					if res["RESPONSE"] == "":
						#0.1秒待ってから入力開始へ
						print("0.1秒待つ")
						time.sleep(0.1)
						break
					else:
						#書き込み
						print(res)
						with open('res.json','w') as fw:
							json.dump(res, fw, indent=4,ensure_ascii=False)
						#ロボット動作と音声合成へ
						##今は仮に
						#音声合成
						jtalk.say(res["RESPONSE"])
						trig = "" ##認識開始前にもどる
						break


# サーバを作成して動かす関数
def socket_work(clientsocket, client_address, client_port):

	while True:
		conn, addr = s.accept()
		print('Connected by', addr)
		recv_data = conn.recv(1024)
		recv_data = recv_data.decode('utf-8')
		recv_data = json.loads(recv_data)

		print(recv_data)
		return recv_data
		conn.close()

if __name__ == '__main__':




	host = "127.0.0.1" #お使いのサーバーのホスト名を入れます
	port = 5000 #クライアントと同じPORTをしてあげます


	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = 'localhost'
	port = 5000
    serversocket.bind((host, port))

    serversocket.listen(128)

    while True:
		# スレッドの作成と開始
	    mythread = chat()
	    mythread.start()

        clientsocket, (client_address, client_port) = serversocket.accept()
        print('New client: {0}:{1}'.format(client_address, client_port))

        # 接続してきたクライアントを処理するスレッドを用意する
        client_thread = threading.Thread(target=socket_work,
                                         args=(clientsocket,
                                               client_address,
                                               client_port))
        # 親 (メイン) スレッドが死んだら子も道連れにする
        client_thread.daemon = True
        # スレッドを起動する
        client_thread.start()
    	# サーバを作成して動かす
    	recv_data = client_thread
