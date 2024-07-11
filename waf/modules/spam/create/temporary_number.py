import requests
from bs4 import BeautifulSoup
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "temporary_number",
        "title"       : "Make a number phone",
        "module"      : "spam/create/temporary_number",
        "description" : "Create a temporary phone number to receive messages"
}

var.ltype  = ['list']

options ={
  "NUMBER" : [str(var.number[0]),'The listen address'],
  "LTYPE"  : [str(var.ltype[0]),'Choose list or create <list / create>']
}


def running():
        try:
                if var.ltype[0] == "list" or var.ltype[0] == "LIST" :

                        print (blue+"[*]"+default+"starting scan your number")
                        url_fake = "http://receivefreesms.net/"
                        face_mail = requests.get(url_fake,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
                        soup = BeautifulSoup(face_mail.content,"html.parser")
                        print (green+"[+]"+default+'Available numbers')

                        for div  in soup.find_all("div",{"class":"cuadro"}):
                                nm = div.a.text.strip('+')
                                print (green+"[+]"+default+"the nember is : "+nm)

                elif var.ltype[0] == "create" or var.ltype[0] == "CREATE":
                        print (blue+"[*]"+default+"creating your number ")
                        try :
                                while True:
                                        url = "http://receivefreesms.net/free-sms-"+str(var.number[0])+".html"
                                        re = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
                                        soup2 = BeautifulSoup(re.content,"html.parser")
                                        fr = soup2.find("td",{"data-title":"From Number"})
                                        from_nember = fr.text.strip('if(location.href.indexOf("receivefreesms")<=0){ alert("STOP stealing my numbers!"); document.location="http://receivefreesms.net/"; }')
                                        ti = soup2.find("td",{"data-title":"Time"})
                                        time = ti.text
                                        mess = soup2.find("td",{"data-title":"Message"})
                                        message = mess.text
                                        print (" ____________________________________________________________________________________________")
                                        print ("|   set nember     |  +"+str(var.number[0]))
                                        print ("|__________________|_________________________________________________________________________|")
                                        print ("|   From Number    |  "+from_nember)
                                        print ("|__________________|_________________________________________________________________________|")
                                        print ("|      Time        |  "+time)
                                        print ("|__________________|_________________________________________________________________________|")
                                        print ("|    Message       |  "+message)
                                        print ("|__________________|_________________________________________________________________________|")
                                        input('')
                                        print (blue+"[*]"+default+"reload")
                        except :
                                        print("\n")
                                        print(red+"[-]"+default+"Unknown error")
                                        print(blue+"[*]"+default+"Check available numbers")
                                        running()
                else:
                        print (red+"[-]"+default+"Choose LTYPE " )
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
