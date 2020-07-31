#!/usr/bin/python

import re , urllib2 , sys , os
from platform import system


logo = '''

    ___    __    __ 
   /   |  / /   / /   | ----| All Sites Grabber |----
  / /| | / /   / /    | Author : MatriX Coder
 / ___ |/ /___/ /___  | FB : www.fb.com/matrixcoder2
/_/  |_/_____/_____/  | Blog : www.matrixcoder.co.vu
                    
'''

# found this code on stackoverflow.com/questions/19278877
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]

print(logo)

class All :
	allsites = []
	i = 0
	def __init__(self, txtfile):
		ips = open(txtfile, 'r').readlines()
		self.length = len(ips)
		for ip in ips :
			ip = ip.rstrip()
			self.bing_all_grabber(ip)
	
	def bing_all_grabber(self, s) :
		#try:
			lista = []
			page = 1
			print('\n')
			All.i += 1
			while page <= 21:
				bing = "http://www.bing.com/search?q=ip%3A"+s+"+&count=50&first="+str(page)
				openbing  = urllib2.urlopen(bing)
				readbing = openbing.read()
				findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
				for i in range(len(findwebs)):
					allnoclean = findwebs[i]
					findall1 = re.findall('http://(.*?)/', allnoclean)
					for idx, item in enumerate(findall1):
							if 'www' not in item:
									findall1[idx]  = 'http://www.' + item + '/'
							else:	
									findall1[idx]  = 'http://' + item + '/'
					lista.extend(findall1)

				page = page + 10
			self.final = unique(lista)
			self.output()
		#except :
		#	pass
	
	def output(self) :
		All.allsites.extend(self.final)
		print ' [+] Grabbed ', len(All.allsites)
		if self.length == All.i :
			# write out 
			outfile = open('outfile.txt', 'w')
			outfile.write('\n'.join(All.allsites))
			# printing out
			for site in  All.allsites :
				print site
			

try :
	All(sys.argv[1])
except IndexError :
	print "[*] Usage : python "+sys.argv[0]+" file.txt"
