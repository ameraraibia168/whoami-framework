import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "carcking_handshake",
        "title"       : "Cracking handshake of network ",
        "module"      : "wireless/wifi/attack cracking handshake network  network_manager",
        "description" : "cracking handshake of network"
}

options ={
  "PATH"      : [str(var.all_var['path']),'enter the path of the handshake file'],
  "WORDLIST"  : [str(var.all_var['wordlist']),'enter the path of the wordlist']

}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Starting a crack handshake")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                order = ("aircrack-ng {} -w {}").format(var.all_var['path'],var.all_var['wordlist'])
                geny = os.system(order)
                print("\n")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))







        
