import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "wifi_honeypot",
        "title"       : "Wireless honeypot(Fake AP)",
        "module"      : "wireless/wifi/attack wifi honeypot network  network_manager",
        "description" : "create fake acces point"
}

options ={
  "INTERFACE" : [str(var.all_var['interface']),'enter the interface [wlan0/wlan0mon]'],
  "BSSID"     : [str(var.all_var['bssid']),'enter the FAKE bssid of the target'],
  "ESSID"     : [str(var.all_var['essid']),'enter the FAKE essid of the target'],
  "CHANNEL"   : [str(var.all_var['channel']),'enter the FAKE channel of the network'],
  "OUTPUT"    : [str(var.all_var['output']),'enter the log file location'],
  "ENCRYPT"   : [str(var.all_var['encrypt']),'enter the type of encryptions [unencrypted/WEP/WPA/WPA2]']

}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Creating Fake Access Point ...")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                if var.all_var['encrypt'].lower() == "unencypted":
                    order =("xterm -e airbase-ng -a {} -c {} --essid {} {} > {} ".format(var.all_var['bssid'],var.all_var['channel'],var.all_var['essid'],var.all_var['interface'],var.all_var['output']))
                    os.system(order)
                elif var.all_var['encrypt'].lower() == "wep":
                    order =("xterm -e airbase-ng -a {} -c {} --essid {} {} -W 1 > {} ".format(var.all_var['bssid'],var.all_var['channel'],var.all_var['essid'],var.all_var['interface'],var.all_var['output']))
                    os.system(order)
                elif var.all_var['encrypt'].lower() == "wpa":
                    order =("xterm -e airbase-ng -a {} -c {} --essid {} {} -W 1 -z 2 > {} ".format(var.all_var['bssid'],var.all_var['channel'],var.all_var['essid'],var.all_var['interface'],var.all_var['output']))
                    os.system(order)
                elif var.all_var['encrypt'].lower() == "wpa2":
                    order =("xterm -e airbase-ng -a {} -c {} --essid {} {} -W 1 -Z 4 > {} ".format(var.all_var['bssid'],var.all_var['channel'],var.all_var['essid'],var.all_var['interface'],var.all_var['output']))
                    os.system(order)
                else:
                    print (red+"[-]"+default+"Error : Encryption ID not Found!")
                print("\n")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
