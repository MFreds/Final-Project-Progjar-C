#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:22:13 2021

@author: basuki
"""
import socket
import select
import sys
import threading

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = ''
port = 8082
server.bind((ip_address, port))
server.listen(1)
list_of_clients = []
ready_client = []

def readyclient(conn,addr):
    # print("hi there its me")
#insert the new ready client to list and calculate size of list

    ready_client.append(conn)
    size_ready_client=0
    for y in ready_client:
        
        # print("hi there its me again")
        if y != conn:
            size_ready_client+=1
            print("sum of ready client is: ",size_ready_client+1)
            
           
    # print("aloha")
    message="waiting for other"
    conn.send(message.encode())

def clientthread(conn,addr):
    while True:
        try:
            data = conn.recv(2048).decode()
            
            # ambil data client lalu kirim ke lient lain
            if data:
                #check do client want to find chat person
                if str(data)=="find":
                    readyclient(conn, addr)
                    
                   
            # else:
            #     remove(conn)
        except:
            continue

while True:
    #get connection
    conn, addr = server.accept()
    #put the connection to list
    list_of_clients.append(conn)
    
    #calculate how many connection in list
    size=0
    for x in list_of_clients:
        size+=1
    print(list_of_clients[size-1])
    print(' connected\n')
    print("sum of client is: ",size)
    
    #get in the thread
    threading.Thread(target=clientthread, args=(conn, addr)).start()
    
   
    
conn.close()
