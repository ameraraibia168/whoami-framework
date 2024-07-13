import os ,time
from waf.libs import variable as var
from waf.libs.banner import *
from waf.libs.color  import *
from waf.libs.tools  import *
from waf.interpreter    import *

def use(module):
    try:
        exec("from waf.modules."+str(module)+" import *")
        whoami1 = str(input(default+'WhoAmi '+str(module[:number_folder_name(module)])+'('+red+str(module[number_folder_name(module)+1:])+default+') > '))
        if whoami1[:3] =='set' or whoami1[:4] == 'set ':
            if whoami1 == "set" or whoami1 == "set ":
                print (" set Name current_setting")
            else :
                numm = 0
                for i in whoami1[4:]:
                    if i != ' ':
                        numm = numm + 1
                    else:
                        break
                if  whoami1[4:4+numm].lower() in var.all_var:
                    var.all_var[whoami1[4:4+numm].lower()] = whoami1[5+numm:]
                    print (whoami1[4:4+numm].upper()+" => "+ var.all_var[whoami1[4:4+numm].lower()])
                else:
                    print (red+"[-]"+default+" Unknown Variable")

        elif whoami1[:12] == "show options" or whoami1[:7] == "options":
            print ("\n")
            print ("    options ("+str(module[number_folder_name(module)+1:])+"):\n" )
            print ("        Name             Current Setting                     Description")
            exec("from waf.modules."+str(module)+" import *;global option;option=options")
            if(len(option)!=0):
                for i in option:
                    print(("         {:10s}       {:30s}      {:s}").format(str(i),str(var.all_var[str(i).lower()]),str(option[i][1])))
            else:
                print("\n      NOTE : No options here,Enter run or exploit ")
            print("\n")
        elif whoami1[:16] == "show description" or whoami1[:11] == "description":
            exec("from waf.modules."+str(module)+" import *;global description;description=info['description']")
            print("\n "+str(description)+" \n")

        elif whoami1[:3] == "run" or whoami1[:7] == "exploit":
            exec ("running()")


        elif whoami1[:6] == "search":
            vsearch = whoami1[7:]
            search (str(vsearch.lower()))

        elif whoami1[:4] == 'show':
            if whoami1 == "show" or whoami1 == "show ":
                show_dir()
            elif whoami1[:5] == 'show ':
                show_modules(whoami1[5:len(whoami1)])

        elif whoami1[:3] == 'use':
            uussee="""
Usage: use <name|term|index>


Examples:
  use admin_panel_findler

  use eternalblue
  use <name|index>
     """
            if whoami1 == "use":
                print(uussee)
            elif check_modules(whoami1[4:]):
                use(whoami1[4:])
            else:
                print (red+"[-]"+default+"No results from search")
                print (red+"[-]"+default+"Failed to load module: "+whoami1)
        elif whoami1[:4] == 'exit' or whoami1[:4] == 'quit':
            exit()
        elif whoami1[:4] == 'back' :
            from waf import interpreter;interpreter.WhoAmi()
        else:
            if ((whoami1[:2] == "ls") or (whoami1[:2] == "vi") or (whoami1[:2] == "id") or (whoami1[:2] == "rm") or (whoami1[:2] == "mv") or (whoami1[:2] == "cp") or (whoami1[:2] == "./") or (whoami1[:2] == "id") or (whoami1[:2] == "df") or (whoami1[:2] == "ps") or (whoami1[:3] == "apt") or (whoami1[:3] == "pwd") or (whoami1[:3] == "cat") or (whoami1[:3] == "man") or (whoami1[:4] == "nmap") or (whoami1[:4] == "ping") or (whoami1[:4] == "less") or (whoami1[:4] == "sudo") or (whoami1[:4] == "grep") or (whoami1[:4] == "echo") or (whoami1[:4] == "nano" ) or (whoami1[:5] == "touch") or (whoami1[:5] == "unzip") or (whoami1[:5] == "mkdir") or (whoami1[:5] == "rmdir") or (whoami1[:5] == "clear") or (whoami1[:6] == "whoami") or (whoami1[:6] == "reboot") or (whoami1[:7] == "history") or (whoami1[:8] == "shutdown") or (whoami1[:8] == "ifconfig")):
                print (blue+"[*]"+default+" exec "+whoami1)
                print ("")
                os.system(whoami1)
            elif whoami1[:6] == "banner":
                banner()
            elif whoami1[:2] == "cd":
                print (red+"[-] No path specified "+default)
            elif whoami1 == '':
                use(module)
            elif whoami1[:2] == "os":
                os.system(whoami1[3:])
            elif whoami1[:5] == 'my_ip':
                my_ip()
            elif whoami1[:4] =='help':
                help_help()
            else:
                print (red+"[-] Unknown command: "+default+""+whoami1)
            use(module)
        use(module)
    except KeyboardInterrupt:
        print (default+"  Interrupt: use the 'exit' command to quit")
        use(module)

