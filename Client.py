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
from ftplib import FTP

ip_chat = ''
port_chat = 8082

#connect to server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip_chat, port_chat))