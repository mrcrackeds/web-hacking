#!/usr/bin/python

import mechanize
import cookielib
from bs4 import BeautifulSoup
import os
noFound =  True
while noFound:
	try:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_equiv(True)
		br.set_handle_referer(True)
		br.set_handle_redirect(True)
		cj = cookielib.LWPCookieJar()
		br.set_cookiejar(cj)
		br.open('http://challenge01.root-me.org/programmation/ch8/')
		bs = BeautifulSoup(br.response().read(), 'lxml')
		bs64 = bs.find('img')['src'].split(',')[1]
		img = open('Captcha.png', 'wb')
		img.write(bs64.decode('base64'))
		img.close()
		os.system('gocr -i Captcha.png > found.txt')
		#os.remove('Captcha.png')
		with open('found.txt', 'r') as f:
			cap = f.read()
			cap = cap.rstrip()
		br.select_form(nr=0)
		br.form['cametu'] = cap
		br.submit()
		bs = BeautifulSoup(br.response().read(), 'lxml')
		message = bs.find('p').next.text
		print message
		noFound = False
	except AttributeError:
		print "Can't resolve the captcha"

