import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "scan_network",
        "title"       : "Scan for WPS networks",
        "module"      : "wireless/wifi/wps scan  network  network_manager",
        "description" : "Scan for WPS Networks"
}

options ={
  "INTERFACE" : [str(var.all_var['interface']),'enter the interface [wlan0/wlan0mon]']
}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Starting a scan for WPS networks")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                order = "airodump-ng -M --wps {}".format(var.all_var['interface'])
                geny = os.system(order)
                cmd = os.system("sleep 5 ")
                print("\n")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
