import time,os,webbrowser
from waf.libs.color import *

info = {
        "name"        : "github_account",
        "title"       : "My account github",
        "module"      : "amerr/github_account",
        "description" : "  No description"
}

options = {}

def running():
        try:
                print ("")
                time.sleep(2)
                print (default+'  {'+blue+'Amerlaceset'+default+'}--------{'+blue+'https://github.com/ameraraibia168'+default+'}')
                time.sleep(6)
                webbrowser.open_new('https://github.com/ameraraibia168')
                os.system('termux-open https://github.com/ameraraibia168')
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
