# Greetz to Magnom-Sec Original : http://pastebin.com/8X4Pf4L8
# Wroten in python by MatriX Coder :D

import sys , urllib2 , re

try:
	def check(site):
		if 'http://' not in site:
			site = 'http://' + site
		print('\n')
		print(site)
		resp = urllib2.urlopen(site).read()
		# Check version 
		wpversion = re.search('content="WordPress (.*?)"', resp).group(1)
		# Check official theme 
		wptheme = re.search('wp-content/themes/(.*?)/', resp).group(1)
		# Check official plugin
		wpplugin = re.search('wp-content/plugins/(.*?)/', resp).group(1)
		print ('\tversion ---> ' + wpversion) + ('\n\ttheme ---> ' + wptheme) + ('\n\tplugin ---> ' + wpplugin)

	s = sys.argv[1]
	with open(s) as f:
		sites = f.readlines()
	for site in sites:
		site = site.replace('\n' , '')
		check(site)
except IndexError:
	print('[*] Usage : '+sys.argv[0]+'list.txt')