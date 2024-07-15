import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "scan networks",
        "title"       : "Scan Network [list wifi]",
        "module"      : "wireless/wifi/interface scan network monitor_mode network_manager",
        "description" : "scan list of wifi network"
}

options ={
  "INTERFACE" : [str(var.all_var['interface']),'enter the interface [wlan0/wlan0mon]']

}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Starting a scan network")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("")
                order = "airodump-ng {} -M".format(var.all_var['interface'])
                print(red+"[-]"+default+"When Done Press CTRL+c")
                cmd = os.system("sleep 3")
                geny  = os.system(order)
                cmd = os.system("sleep 8")
                print("\n")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
