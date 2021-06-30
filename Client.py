#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:25:24 2021

@author: basuki
"""
import socket
import select
import sys
from threading import Thread
import os
import socket
import sys
import threading
import time

def baca_pesan(server):
    while True:
        #receive msg
        data = server.recv(65535).decode("utf-8")
        if len(data) == 0:
            break

        print(data)

ip_chat = '127.0.0.1'
port_chat = 8081

username_cli = input('Masukkan Username : ')

#connect to server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip_chat, port_chat))

#send user info to server
server.send(bytes(username_cli, "utf-8"))

#create thread for msg read
thread_cli = threading.Thread(target=baca_pesan, args=(server,))
thread_cli.start()

print("Selamat datang, kamu sudah masuk kedalam chat room!")

while True:

    # send/recv msg
    dest="broadcast"
    message = input()
    server.send(bytes("{}|{}".format(dest, message), "utf-8"))

    #exit
    if message == "exit":
        server.close()
        break
