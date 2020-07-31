#!/usr/bin/env python

# this a simple port scanner using socket module
# Wroten by MatriX Coder

import socket, threading, time

def PortScanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.settimeout(5)
    sock = sock.connect_ex((ip,port))
    if sock == 0:
        print "[*] Port %i is open" % port 
   
if __name__ == '__main__':
	ip = raw_input('Please Enter IP >>> ')
	for i in range(1,1001):
		t = threading.Thread(target=PortScanner, args=(ip, i))
		#PortScanner(ip, i)
		t.start()
		time.sleep(0.1)

