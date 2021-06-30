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
ip_chat = ''
port_chat = 8081

#connect to server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip_chat, port_chat))


def send_msg(sock):
    while True:
        message = input()
        
        sock.send(message.encode()) 
        sys.stdout.write('<You> ')
        sys.stdout.write(message + '\n')
        sys.stdout.flush()
    


# terima dari server
def recv_msg(sock):
    while True:
        data = sock.recv(2048)
        sys.stdout.write(data.decode() + '\n')

Thread(target=send_msg, args=(server,)).start()
Thread(target=recv_msg, args=(server,)).start()


def ready():
    #this thing just testing
    message = input()
    server.send(message.encode())

while True:  
    
    ready()
    
    #list server socket
    socket_list=[server]
    # socket_list=[sys.stdin]
    
    # get from list
    
    ########## uncomment the code for using
    ########## for linux  ##########
    read_socket, write_socket, error_socket = select.select(socket_list, [], [],0)
    
    ########## for windows #########
    # read_socket, write_socket, error_socket = select.select([socket _list], [], [])
    
    # Looping untuk menerima dan mengirim pesan
    for socks in read_socket:
        if socks == server:
            recv_msg(socks)
        # else:
        #     send_msg(socks)
    
server.close()