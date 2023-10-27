
import os,requests,time,sys
from waf.libs.color import *


def help_help():
        print ("")
        print ("Usage Commands     ")
        print ("===============     ")
        print ("    Commands                    Description     ")
        print ("    ------------                -------------     ")
        print ("    help                        Help menu     ")
        print ("    ifconfig                    check my ip with router    ")
        print ("    whoami                      whoami                    ")
        print ("    search                      Search for a library")
        print ("    os                          Run Linux Commands(ex : os ifconfig)")
        print ("    my_ip                       check my ip              ")
        print ("    use                         Select Module For Use     ")
        print ("    clear                       Clear the menu     ")
        print ("    show                        To view the available modules")
        print ("    exit                        Exit            " )
        print ("")

def exit():
        print (blue+"\n[*]"+default+" { exit } Detected, Trying To Exit ...")
        time.sleep(0.5)
        print (blue+"[*]"+default+"Good bay")
        sys.exit()


def my_ip():
        print ("")
        my_ip = requests.get('https://api.myip.com/')
        data = my_ip.json()
        print (basic_green + 'Country       :      ' + white + data['country'] + '[' + data['cc'] + ']')
        print (basic_green + 'my_ip         :      ' + white + data['ip'])




def modules(modules_directory):
    modules = []
    for root, dirs, files in os.walk(modules_directory):
        _, package, root = root.rpartition('waf/modules/'.replace('/', os.sep))
        root = root.replace(os.sep, '.')
        files = filter(lambda x: not x.startswith("__") and x.endswith('.py'), files)
        modules.extend(map(lambda x: '.'.join((root, os.path.splitext(x)[0])), files))
    return modules



def search(y):
        module = modules("waf/modules/")
        boolean = True
        num = 1
        for i in module :
                exec("from waf.modules."+str(i)+" import *;global valeur,title;valeur = info['module'];title=info['title']")
                if (str(y) in valeur):
                        if boolean :
                                        print ("")
                                        print (y)
                                        print ("==========")
                                        print ("    #   Name                                                            Title")
                                        print ("    -   ----                                                            -----")
                                        boolean = False
                        print(("  {:03d}   {:64s}{:s}").format(num,str(i),str(title)))
                        num = num + 1
        if boolean:
                        print (red+"[-]"+default+"No results from search")
                        print (red+"[-]"+default+"Failed to load module: "+y)
        print("")



def show_modules(y):
                module = modules("waf/modules/"+y)
                if len(module) != 0 :
                                        y = str(y)
                                        num = 1
                                        print ("")
                                        print (y)
                                        print ("==========")
                                        print ("    #   Name                                                            Title")
                                        print ("    -   ----                                                            -----")
                                        for i in module:
                                                exec("from waf.modules."+str(i)+" import *;global valeur,title;valeur = info['module'];title=info['title']")
                                                print(("  {:03d}   {:64s}{:s}").format(num,str(i),str(title)))
                                                num = num +1
                                        print("")
                else:
                        print (red+"[-]"+default+"No results from search")
                        print (red+"[-]"+default+"Failed to load module: "+y)


def show_dir():
                print ("")
                print ("Usage Commands")
                print ("===============")
                print ("    Commands                    Description")
                print ("    ------------                -------------")
                print ("    show exploits               Show Backdoors of Current Database")
                print ("    show auxiliary              Show Encoders(Py,Ruby,PHP,Shellcode etc..)")
                print ("    show network                Show Network Services")
                print ("    show payloads               Show Injectors(Shellcode,dll,so etc..)")
                print ("    show wireless               show Wireless(attack,oin,wps..)")
                print ("    show spam                   Show Spam(fake,..)")
                print ("    show amerr                  Show My Information")
                print ("")


def check_modules(y):
        module = modules("waf/modules")
        if (str(y) in module):
                return True
        else:
                return False


def number_folder_name(m):
        n=0
        for i in m:
                if i != ".":
                        n = n + 1
                else:
                        break
        return n

