
# coding: utf-8

# In[17]:

# run a client
def client(ip_list, username_list, password_list, local_ip, port):
    import subprocess
    
    processes = set()
    
    for i in range(len(ip_list)):
        print("working on subprocess", i)
        processes.add(subprocess.Popen(['sh', 'login.sh' , str(ip_list[i]), str(username_list[i]), str(password_list[i]), str(local_ip), str(port)]))
        print("finish working on subprocess", i)

        
        


# In[18]:

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

ip_list = []
user_name_list = []
password_list = []

ip_list.append("140.119.65.87")
user_name_list.append("jacky18008")
password_list.append("Samsungace3")

ip_list.append("140.119.65.135")
user_name_list.append("mathlab115")
password_list.append("math701")

client(ip_list, user_name_list, password_list, local_ip, port)


# In[4]:

ip_list


# In[ ]:



