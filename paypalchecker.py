#!/usr/bin/python

import urllib2 , re , cookielib, time
import threading

emailslist = []

def PaypalChecker(ss):
    check = re.compile("Country or region" , re.I)
    baseurl = "https://www.paypal.com/cgi-bin/webscr?cmd=_send-money&myAllTextSubmitID=&cmd=_send-money&type=external&payment_source=p2p_mktgpage&payment_type=Gift&sender_email="+ss+"&email=gz%40s.com&currency=USD&amount=10&amount_ccode=USD&submit.x=Continue"
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
    #print hmmm
    if len(hmmm) != 0:
            print "[*] %s ==> NO" % ss
            nowrite.write(ss)
            nowrite.write('\n')
            nowrite.close()
    else:
            print "[*] %s ==> YES" % ss
            yeswrite.write(ss)
            yeswrite.write('\n')
            yeswrite.close()

    return

textfile = raw_input("Enter Text File >>> ")

with open(textfile , "r") as f:
    emails = f.readlines()
    
for email in emails:
    email = email.rstrip('\n')
    emailslist.append(email)

yeswrite = open('YES.txt' , 'a')
nowrite = open('NO.txt' , 'a')
print "\n"
print "\n"
print "Emails To Check : " + str(len(emailslist))
print "\n"
#threads = []
for em in emailslist:
    # Parallel Multithreading The Easy way using threading module
    t = threading.Thread(target=PaypalChecker, args=(em,))
    t.start()
    time.sleep(2)