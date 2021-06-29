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
server.listen(100)

while True:
    conn, addr = server.accept()
    
    if conn:
        print("connected from: ", conn)
    
conn.close()
