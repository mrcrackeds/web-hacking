#!/usr/bin/python

#  >>>>>>>>> bismallah <<<<<<<<<<
# Coded by MatriX Coder | matrix.coder1@gmail.com
# You are free to edit my code and to remove my rights :D
# But it won't make you the coder
# Greetz to fallega team | www.dev-tun.tn
# Idea from here http://www.madleets.com/Thread-Get-The-IP-Behind-Cloudflare

'''
this is simple script that 
'should' bypass cloudflare
with really simple methods
'''

import sys , os , socket
from platform import system

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
    
logo = '''
   ________                ________               
  / ____/ /___  __  ______/ / __/ /___ _________   | ---| Cloudflare Bypasser |---
 / /   / / __ \/ / / / __  / /_/ / __ `/ ___/ _ \  | Author : MatriX Coder
/ /___/ / /_/ / /_/ / /_/ / __/ / /_/ / /  /  __/  | FB : www.fb.com/matrixcoder2
\____/_/\____/\__,_/\__,_/_/ /_/\__,_/_/   \___/   | Blog : www.matrixcoder.co.vu

                                                                               
'''

print logo 

try:
	subdoms = ['webmail' , 'ftp' , 'direct' , 'cpanel'] # really simple :D
	site = sys.argv[1]
	# Cleaning the sh*t
	if 'http://' in site:
		site = site.replace('http://' , '')
	if 'www' in site :
		site  = site.replace('www' ,'')
	if site[-1] == '/':
		site[-1] = ''
		
	ip = socket.gethostbyname(site)
	
	for subdom in subdoms:
		doo = subdom + '.' + site
		try:
			ddd = socket.gethostbyname(doo)
			if ip != ddd:
				print '\n' + site + ' : Found ---> ' + ddd + '\n'
			else :
				print 'Not found :('
		except:
			pass
	
	
	
except IndexError:
	print "[*] Usage : python "+sys.argv[0]+" domain.com"