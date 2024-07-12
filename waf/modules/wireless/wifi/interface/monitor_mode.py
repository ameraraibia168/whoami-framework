import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "monitor_mode",
        "title"       : "[start/stop] monitor mode ",
        "module"      : "wireless/wifi/interface monitor_mode network_manager",
        "description" : "wireless wifi [start/stop] interface monitor mode"
}

options ={
  "INTERFACE" : [str(var.interface[0]),'enter the interface [wlan0/wlan0mon]'],
  "MODE"      : [str(var.mode[0]),'enter the mode [start/stop]']

}

def running():
        try:
                if var.mode[0] == 'start' :
                        print ("")
                        print (blue+"[*]"+default+ "Starting a monitor mode")
                        time.sleep(2)
                        print ("")
                        time.sleep(2)
                        print ("")
                        order = "airmon-ng start {} && airmon-ng check kill".format(var.interface[0])
                        geny  = os.system(order)
                        print("\n")
                        print (green_underline+"[*] Done"+default)
                        time.sleep(2)
                        print ("")
                elif var.mode[0] == 'stop' :
                        print ("")
                        print (blue+"[*]"+default+ "Stoping a monitor mode")
                        time.sleep(2)
                        print ("")
                        time.sleep(2)
                        print ("")
                        order = "airmon-ng stop {} && service network-manager restart".format(var.interface[0])
                        geny  = os.system(order)
                        print("\n")
                        print (green_underline+"[*] Done"+default)
                        time.sleep(2)
                        print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
