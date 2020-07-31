#!/usr/bin/python

# all websites grabber

'''

888b     d888  .d8888b.
8888b   d8888 d88P  Y88b
88888b.d88888 888    888
888Y88888P888 888
888 Y888P 888 888
888  Y8P  888 888    888
888   "   888 Y88b  d88P
888       888  "Y8888P"

Coded by MatriX Coder from tunisia
Use my code as you want :D    

'''

import re , urllib2 , sys , os
from platform import system

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')

logo = '''

    ___    __    __ 
   /   |  / /   / /   | ----| All Sites Grabber |----
  / /| | / /   / /    | Author : MatriX Coder
 / ___ |/ /___/ /___  | FB : www.fb.com/matrixcoder2
/_/  |_/_____/_____/  | Blog : www.matrixcoder.co.vu
                    

[*] Usage : python '''+sys.argv[0]+''' 127.0.0.1
'''

# found this code on stackoverflow.com/questions/19278877
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]

print(logo)
try:
	lista = []
	s = sys.argv[1]
	page = 1
	print('\n')
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

	saveinfile = open('sites.txt' , 'a')
	final =  unique(lista)
	for all1 in final:
		print(all1)
		saveinfile.write(all1)
		saveinfile.write('\n')

	try:
		for i , l in enumerate(final):
			pass
		print '\nSites Found : ' , i + 1
	except:
		pass

except IndexError:
	pass