import socket,os,sys,select
from waf.libs.color  import *
from waf.libs import variable as var

info = {
        "name"        : "private_communication_server",
        "title"       : "Simple local chat",
        "module"      : "auxiliary/private_communication_server",
        "description" : "Simple local chat"
}

options ={
  "LHOST" : [str(var.all_var['lhost']),'The listen address'],
  "LPORT" : [str(var.all_var['lport']),'The listen port'],
  "LTYPE" : [str(var.all_var['ltype']),'Choose server or connect <server / client>']
}

class Server(object):
     # List to keep track of socket descriptors
     CONNECTION_LIST = []
     RECV_BUFFER = 4096  # Advisable to keep it as an exponent of 2
     PORT = int(var.all_var['lport'])
     HOST = str(var.all_var['lhost'])
     def __init__(self):
        self.user_name_dict = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_up_connections()
        self.client_connect()

     def set_up_connections(self):
        # this has no effect, why ?
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(50)  # max simultaneous connections.


        # Add server socket to the list of readable connections
        self.CONNECTION_LIST.append(self.server_socket)

    # Function to broadcast chat messages to all connected clients
     def broadcast_data(self, sock, message):
        # Do not send the message to master socket and the client who has send us the message
        for socket in self.CONNECTION_LIST:
            if socket != self.server_socket and socket != sock:
                # if not send_to_self and sock == socket: return
                try:
                    socket.send(message)
                except:
                    # broken socket connection may be, chat client pressed ctrl+c for example
                    socket.close()
                    self.CONNECTION_LIST.remove(socket)

     def send_data_to(self, sock, message):
        try:
            sock.send(message)
        except:
            # broken socket connection may be, chat client pressed ctrl+c for example
            socket.close()
            self.CONNECTION_LIST.remove(sock)

     def client_connect(self):
        print (blue+"[*]"+default+"Chat server started on port " + str(self.PORT))
        while 1:
            # Get the list sockets which are ready to be read through select
            read_sockets, write_sockets, error_sockets = select.select(self.CONNECTION_LIST, [], [])

            for sock in read_sockets:
                # New connection
                if sock == self.server_socket:
                    # Handle the case in which there is a new connection recieved through server_socket
                    self.setup_connection()
                # Some incoming message from a client
                else:
                    # Data recieved from client, process it
                    try:
                        # In Windows, sometimes when a TCP program closes abruptly,
                        # a "Connection reset by peer" exception will be thrown
                        data = sock.recv(self.RECV_BUFFER)
                        if data:
                            if self.user_name_dict[sock].username is None:
                                self.set_client_user_name(data, sock)
                            else:
                                self.broadcast_data(sock, "\r" + ' { ' + self.user_name_dict[sock].username + ' }>>>' + data)

                    except:
                        self.broadcast_data(sock, red+"[-]"+default+"Client (%s, %s) is offline" % addr)
                        print (red+"[-]"+default+"Client (%s, %s) is offline" % addr)
                        sock.close()
                        self.CONNECTION_LIST.remove(sock)
                        continue

        self.server_socket.close()

     def set_client_user_name(self, data, sock):
        self.user_name_dict[sock].username = data.strip()
        self.send_data_to(sock, data.strip() + ', you are now in the chat room\n')
        self.send_data_to_all_regesterd_clents(sock, data.strip() + ', has joined the cat room\n')

     def setup_connection(self):
        sockfd, addr = self.server_socket.accept()
        self.CONNECTION_LIST.append(sockfd)
        print (blue+"[*]"+default+"Client (%s, %s) connected" % addr)
        self.send_data_to(sockfd, blue+"[*]"+default+"please enter a username: ")
        self.user_name_dict.update({sockfd: Connection(addr)})

     def send_data_to_all_regesterd_clents(self, sock, message):
        for local_soc, connection in self.user_name_dict.iteritems():
            if local_soc != sock and connection.username is not None:
                self.send_data_to(local_soc, message)

class Connection(object):
    def __init__(self, address):
        self.address = address
        self.username = None



def prompt():
    sys.stdout.write("> ")
    sys.stdout.flush()


class Client(object):
    def __init__(self):
        self.host = str(var.all_var['lhost'])
        self.port = int(var.all_var['lport'])
        self.sock = None
        self.connect_to_server()

    def connect_to_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2)
        # connect to remote host
        try:
            self.sock.connect((self.host, self.port))
        except:
            print (blue+'[*]'+default+'Unable to connect')
        print (blue+'[*]'+default+'Connected to remote host. Start sending messages')
        prompt()
        self.wait_for_messages()

    def wait_for_messages(self):
        while 1:
            socket_list = [sys.stdin, self.sock]

            # Get the list sockets which are readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

            for sock in read_sockets:
                # incoming message from remote server
                if sock == self.sock:
                    data = sock.recv(4096)
                    if not data:
                        print (red+'\n[-]'+default+'Disconnected from chat server')
                    else:
                        # print data
                        sys.stdout.write(data)
                        prompt()

                # user entered a message
                else:
                    msg = sys.stdin.readline()
                    self.sock.send(msg)
                    prompt()

def running():
        try:
                if (var.all_var['ltype'].lower() == "server"):
                        Server()
                elif (var.all_var['ltype'].lower() == "client"):
                        Client()
                else :
                        print (red+"[-]"+default+"Choose LTYPE " )
        except Exception as e:
                print(red+"\n[-]"+default+"Error : "+str(e))
