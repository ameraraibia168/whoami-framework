import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "monitor_mode",
        "title"       : "[Start/Stop] monitor mode ",
        "module"      : "wireless/wifi/interface monitor_mode network_manager",
        "description" : "wireless wifi [start/stop] interface monitor mode"
}

options ={
  "INTERFACE" : [str(var.all_var['interface']),'enter the interface [wlan0/wlan0mon]'],
  "MODE"      : [str(var.all_var['mode']),'enter the mode [start/stop]']

}

def running():
        try:
                if var.all_var['mode'].lower() == 'start' :
                        print ("")
                        print (blue+"[*]"+default+ "Starting a monitor mode")
                        time.sleep(2)
                        print ("")
                        time.sleep(2)
                        print ("")
                        order = "airmon-ng start {} && airmon-ng check kill".format(var.all_var['interface'])
                        geny  = os.system(order)
                        print("\n")
                        print (green_underline+"[*] Done"+default)
                        time.sleep(2)
                        print ("")
                elif var.all_var['mode'].lower() == 'stop' :
                        print ("")
                        print (blue+"[*]"+default+ "Stoping a monitor mode")
                        time.sleep(2)
                        print ("")
                        time.sleep(2)
                        print ("")
                        order = "airmon-ng stop {} && service network-manager restart".format(var.interface[0])
                        geny  = os.system(order)
                        print("\n")
                        print (green_underline+"[+] Done"+default)
                        time.sleep(2)
                        print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
