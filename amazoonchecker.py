#!/usr/bin/python

import urllib2 , re , cookielib

emailslist = []

def AmazoonChecker(ss):
    yeswrite = open('YES.txt' , 'w')
    nowrite = open('NO.txt' , 'w')
    check = re.compile("You indicated" , re.I)
    baseurl = "https://www.amazon.com/ap/register?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dgno_newcust?&email=" + ss
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),
    ('Accept-Encoding', 'none'),
    ('Accept-Language', 'en-US,en;q=0.8'),
    ('Connection', 'keep-alive')
    ]
    
    #req = urllib2.Request(baseurl , headers=hdr)
    #html = urllib2.urlopen(req).read()
    ssss = opener.open(baseurl)
    html = ssss.read()
    hmmm = re.findall(check , html)
    if len(hmmm) != 0:
        print "[*] %s ==> YES" %ss
        yeswrite.write(ss)
        yeswrite.write('\n')
    else:
        print "[*] %s ==> NO" %ss
        nowrite.write(ss)
        nowrite.write('\n')

textfile = raw_input("Enter Text File : ")

with open(textfile , "r") as f:
    emails = f.readlines()
    
for email in emails:
    email = email.rstrip('\n')
    emailslist.append(email)
    
for em in emailslist:
    AmazoonChecker(em)
    