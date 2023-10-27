import os,time,webbrowser
from waf.libs.color import *

info = {
        "name"        : "facebook_account",
        "title"       : "My account facebook",
        "module"      : "amerr/facebook_account",
        "description" : "  No description"
}


options ={}


def running():
        try:
                print ("")
                time.sleep(2)
                print (default+'  {'+blue+'Amer Amer'+default+'}--------{'+blue+'https://www.facebook.com/100019536310282'+default+'}')
                time.sleep(6)
                webbrowser.open_new('https://www.facebook.com/100019536310282')
                os.system('termux-open https://www.facebook.com/100019536310282')
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
