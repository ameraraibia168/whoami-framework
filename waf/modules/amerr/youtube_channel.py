import webbrowser,time
from waf.libs.color import *

info = {
        "name"        : "youtube_channel",
        "title"       : "My channel youtube",
        "module"      : "amerr/youtube_channel",
        "description" : "  No description"
}

options = {}

def running():
        try:
                print ("")
                time.sleep(2)
                #print default+'  {'+red+'Virus4 Hacking'+default+'}--------{'+red+'https://www.youtube.com/channel/UCmQETFbkmkiSiu3og6F8usg'+default+'}'
                time.sleep(6)
                #webbrowser.open_new('https://www.youtube.com/channel/UCmQETFbkmkiSiu3og6F8usg')
                #os.system("termux-open https://www.youtube.com/channel/UCmQETFbkmkiSiu3og6F8usg ")
                print ("no channel :(")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
