from urllib.error        import *
from urllib.request      import *
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "panel_findler",
        "title"       : "Admin panel",
        "module"      : "auxiliary/admin/panel_findler",
        "description" : "Searching admin panel"
}

options ={
  "LINK" : [str(var.link[0]),'link web target']
}

def running():
        try:
                f = open("waf/resources/link.txt","r");
                link = var.link[0]
                print (blue+"[*]"+default+"starting the scanning")
                print ("\n\nAvilable links : \n")
                while True:
                        sub_link = f.readline()
                        if not sub_link:
                                break
                        req_link = ("http://"+link+"/"+sub_link)
                        req = Request(req_link)
                        try:
                                response = urlopen(req)
                        except HTTPError as e:
                                continue
                        except URLError as e:
                                        continue
                        else:
                                print ("OK => ",req_link)
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
