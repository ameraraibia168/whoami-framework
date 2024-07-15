import time,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "show_interfaces",
        "title"       : "Show list interfaces_available",
        "module"      : "wireless/wifi/interface show network_manager",
        "description" : "it provides you with the service of displaying the available interfaces"
}

options ={
}

def running():
        try:
                print ("")
                print (blue+"[*]"+default+ "Search for interfaces")
                time.sleep(2)
                print ("")
                time.sleep(2)
                print ("")
                order = "netstat -i"
                geny  = os.system(order)
                print("")
                print (green_underline+"[+] Done"+default)
                time.sleep(2)        
                print ("")
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
