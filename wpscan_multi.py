#!/usr/bin/python

#  >>>>>>>>> bismallah <<<<<<<<<<
# Coded by MatriX Coder | matrix.coder1@gmail.com
# You are free to edit my code and to remove my rights :D
# But it won't make you the coder
# Greetz to fallega team | www.dev-tun.tn

'''
this is simple script that 
enables multi scan in wpscan
'''

import sys , os , subprocess
from platform import system

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
    
logo = '''

 _       ______                      
| |     / / __ \______________ _____    | ----| WPscan Multi |----
| | /| / / /_/ / ___/ ___/ __ `/ __ \   | Author : MatriX Coder
| |/ |/ / ____(__  ) /__/ /_/ / / / /   | FB : www.fb.com/matrixcoder2
|__/|__/_/   /____/\___/\__,_/_/ /_/    | Blog : www.matrixcoder.co.vu
                                     
'''

# checks if wpscan.rb exists
s = os.path.isfile('wpscan.rb')
if not s == True:
	print 'wpscan.rb not found check it please !'
	exit()

print logo

try:
	def lob(site):
		site = site.rstrip()
		scansite = 'ruby wpscan.rb --url %s' % site
		p = subprocess.Popen(scansite, shell=True, stderr=subprocess.PIPE)
		out = p.stderr.read(1)
		print out
		
	file1 = open(sys.argv[1] , 'r')
	sites = file1.readlines()
	for site in sites:
		lob(site)

except IndexError:
	print "[*] Usage : python "+sys.argv[0]+" wp.txt"