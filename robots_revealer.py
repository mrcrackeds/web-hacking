#!/usr/bin/env python

try :
    import requests
except ImportError :
    print "[-] You need to install requests!"
    exit()

requests.packages.urllib3.disable_warnings()

class robots(object) :

    text = ""

    def __init__(self, website) :
        self.website = self.__prepare(website)

    def __prepare(self, website) :
        if "robots.txt" not in website :
            return website+"/robots.txt"

    def __make(self) :
        try :
            a = requests.get(self.website)
            return a.text
        except :
            return None

    def getRobots(self) :
        self.text = self.__make()

    def parseRobots(self, text) :
        dirs = []
        for line in text.splitlines() :
            a = line.find("Disallow")
            if a != -1 :
                dirs.append(line[a+10:])
        return dirs


rob = robots(raw_input("Enter Website : "))
rob.getRobots()
if rob.text != None :
    dirs = rob.parseRobots(rob.text)
    print "[*] Found, "+str(len(dirs))+" directorys."
    for dire in dirs :
        print dire
