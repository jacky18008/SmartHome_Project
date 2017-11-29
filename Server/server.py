import time
import socket
    
import os
import json
import utils 
from pprint import pprint
import sys

from threading import Thread
import socket
import threading
import socketserver

import subprocess


"""
# make it as a function to implement multi-thread
class client_thread(Thread):
    
    def __init__(self, client_socket, thread_index):
        super(client_thread, self).__init__()
        self.client_socket = client_socket
        self.thread_index = thread_index
    
        print("working on thread", self.thread_index, "......")
        
    def device_repair():
        import time
        print("device repairing......")
        time.sleep(10)
        
    def __run__():
    
        #listen for client 
        print("listen for client ", self.thread_index)
        uploaded_file = 0
        order_string = ""

        #if client hasn't sent files, request it to send
        if uploaded_file == 0:
            
            print("client ", self.thread_index, "hasn't sent data, asking to send......")

            # command client to send files
            order_string = "send files"
            self.client_socket.send(order_string.encode('UTF-8'))

            number_of_files = (self.client_socket.recv(1024))
            number_of_files = int(number_of_files.decode('UTF-8'))

            print("receiving ", number_of_files, "files......")

            for i in range(number_of_files):

                #get file name and decode it
                file_name = self.client_socket.recv(1024)
                file_name = file_name.decode('UTF-8')
                print ("Opening file - ",file_name)

                # make a new file and edit it in local 
                fp = open(file_name, 'w')
                #file_name = fp.name
                print("file_name", file_name)

                # keep getting partial data for the limit length of TCP/IP 
                while True:
                    cont = self.client_socket.recv(1024)
                    cont = cont.decode('UTF-8')
                    if  cont == 'EOF':
                        break

                    fp.write(cont)

                fp.flush()
                fp.close()

                home_name = "HsienHao's Home"
                with open(file_name) as device_file:
                    device = json.load(device_file)
                    pprint(device)
                    index.InsertFiles(device_file, home_name)

            uploaded_file = 1



        #routine check for client
        order_string = "check device"
        self.client_socket.send(order_string.encode('UTF-8'))
        device_situation = self.client_socket.recv(1024)

        # if not device not work normally, then execute self-repaired function
        if device_situation != "work normally":
            device_repair()

"""

#repair function
def device_repair():
    import time
    print("device repairing......")
    time.sleep(10)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        #listen for client 
        cur_thread = threading.current_thread()
        print("listen for client ", cur_thread)
        uploaded_file = 0
        order_string = ""


        #if client hasn't sent files, request it to send
        if uploaded_file == 0:
            
            print("client ", """self.thread_index,""" "hasn't sent data, asking to send......")

            # command client to send files
            order_string = "send files"
            self.request.send(order_string.encode('UTF-8'))

            number_of_files = self.request.recv(1024)
            number_of_files = int(number_of_files.decode('UTF-8'))
            print("type of number_of_files", type(number_of_files))

            print("receiving ", number_of_files, "files......")

            for i in range(number_of_files):

                #get file name and decode it
                file_name = self.request.recv(1024)
                file_name = file_name.decode('UTF-8')
                print ("Opening file - ",file_name)

                # make a new file and edit it in local 
                with open(file_name, 'w') as fp:
                #file_name = fp.name
                    print("file_name of opening file: ", file_name)

                # keep getting partial data for the limit length of TCP/IP 
                    while True:
                        cont = self.request.recv(1024)
                        cont = cont.decode('UTF-8')
                        if  cont == 'EOF':
                            break

                        fp.write(cont)

                    fp.flush()
                    print("finish writing of ", file_name)
                    fp.close()

                home_name = "HsienHao's Home"
                with open(file_name, 'r') as device_file:
                    device_data = str(json.load(device_file))
                    #pprint(device_data)
                    index.InsertFiles(device_file, home_name, device_data)
                    
                    device_file.close()
                
                print(file_name, "sent.")

            uploaded_file = 1



        #routine check for client
        order_string = "check device"
        self.request.send(order_string.encode('UTF-8'))
        device_situation = self.request.recv(1024)

        # if not device not work normally, then execute self-repaired function
        if device_situation != "work normally":
            device_repair()


        

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

# run a client
def client(ip, username, password, local_ip, port):
    import subprocess
    print("working on subprocess")
    process = subprocess.run(['sh', 'login.sh' , str(ip), str(username), str(password), str(local_ip), str(port)])
    print("finish working on subprocess")
    
        
    
#main function
if __name__ == "__main__":
    import time
    import socket
    import threading
    import socketserver
    

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 0))
    
    #number of server can hold
    server_socket.listen(1024)
    
    #get current port, set host.
    local_ip = server_socket.getsockname()[0]
    port = server_socket.getsockname()[1]
    print ("current_port: ", port)
    host = "localhost"

        
    #make the path of index if do not exist
    file_path = os.path.join(os.getcwd(), "Data")
    if not os.path.isdir(file_path):#check if path exists, else, make the path.
        print("path does not exist, creating a new one...") 
        os.makedirs(file_path)

    #check if the index exist, else make a new one.    
    index_path = os.path.join(file_path, "index.json")
    if not os.path.isfile(index_path):
        print("file does not exist, creating a new one...") 
        index_p = open(index_path, 'w')

    #create a class of SmartHomeIndex
    index = utils.SmartHomeIndex(index_path)
    print("index_path: ", index_path)
    
    
    #initial a multi client server
    
    #host, port = "localhost", 0
    #print("initialling server......")
    #server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
    

    #local_ip, port = server.server_address
    
    #print("local_ip: ", local_ip, ", port: ", port)
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    #server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    #server_thread.daemon = True
    #server_thread.start()
    #print("Server loop running in thread:", server_thread.name)

    #print("ready to get clients")
    
    #dir_path = "/Users/hsienhaochen/Documents/專題_張宏慶老師/Codes_2/Client/"
    #client_script_name = "client.py"

    #address_1 = dir_path+client_script_name
    #address_2 = dir_path+client_script_name

    #ip = "172.20.10.6"
    #user_name = "pi"
    #password = "00000000"

    ip = "140.119.65.87"
    user_name = "jacky18008"
    password = "Samsungace3"
    

    client(ip, user_name, password, local_ip, port)
    #client(ip, port)
        


        #finish getting clients

"""
    count = 0
    while(1):
        
        # A list of whole threads
        thread_list = []
        
        # initial a client
        client_socket, address = server_socket.accept()
        print ("Conencted to - ",address,"\n")
        count += 1
        
        # call a new thread for each client.
        new_thread = client_thread(client_socket, count)
        new_thread.start()
        new_thread.run()
"""
        
        
        
        
    
