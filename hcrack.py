#!/usr/bin/python

# simple hash cracker working with wordlist
# just for Fun !

'''

888b     d888  .d8888b.
8888b   d8888 d88P  Y88b
88888b.d88888 888    888
888Y88888P888 888
888 Y888P 888 888
888  Y8P  888 888    888
888   "   888 Y88b  d88P
888       888  "Y8888P"

Coded by MatriX Coder from tunisia
Use my code as you want :D

'''

import hashlib , sys , os
from platform import system

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')

logo = '''

    __  __                     __  
   / / / /_____________ ______/ /__  | ----| Hcrack |----
  / /_/ / ___/ ___/ __ `/ ___/ //_/  | Author : MatriX Coder
 / __  / /__/ /  / /_/ / /__/ ,<     | FB : www.fb.com/matrixcoder2
/_/ /_/\___/_/   \__,_/\___/_/|_|    | Blog : www.matrixcoder.co.vu
                                   


Supported algo : md5 | sha1
[*] Usage : python '''+sys.argv[0]+''' hash  algo wordlist.txt
'''

print(logo)


def md5(hash1 , pass1):
    crypted = hashlib.md5(pass1).hexdigest()
    if crypted != hash1:
        print(hash1 + ' != ' + str(crypted))
    elif crypted == hash1:
        print('\t\n----> Cracked : ' + pass1 + '\n')
        exit()
    
def sha1(hash1 , pass1):
    crypted = hashlib.sha1(pass1).hexdigest()
    if crypted != hash1:
        print(hash1 + ' != ' + str(crypted))
    elif crypted == hash1:
        print('\t\n----> Cracked : ' + pass1 + '\n')
        exit()
    


try:
    wordlist = sys.argv[3]
    sss = open(wordlist , 'rb')
    passes = sss.readlines()
    for pass1 in passes:
        pass1 = pass1.replace('\n' , '')
        algo = sys.argv[2]
        hash1 = sys.argv[1]
        if algo == 'md5':
            md5(hash1 , pass1)
        if algo == 'sha1':
            sha1(hash1 , pass1)
except IndexError:
    pass