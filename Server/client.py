
#!/usr/bin/python
# TCP client example


def device_check():
    import time
    print("checking devices......")
    time.sleep(2)
    
    device_situation = "work normally"
    
    return device_situation



#main function    
if __name__ == "__main__":
    import time
    import socket,os
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #use command line arguments to get port
    import argparse

    parser = argparse.ArgumentParser(description='Self management of smart home.')
    parser.add_argument('ip', type=str, help='server ip')
    parser.add_argument('port', type=str, help='port to the server.')

    #port = int(input("client port?"))

    #parse arguments
    args = parser.parse_args()
    ip = args.ip
    port = int(args.port)

    client_socket.connect((ip, port))

    #check if get the port from python subprocess.
    print("get port", port)

    k = ' '
    size = 1024



    #get command from client
    #order_string = client_socket.recv(1024)
    #order_string = order_string.decode('UTF-8')

    #new device, hasn't sent files
    #if order_string == "send files":

    #find all json files and send

    #list it first 
    json_list = []
    import os
    for files in os.listdir(os.getcwd()):
        if files.endswith(".json"):
            json_list.append(files)
    print("has to send ", len(json_list), "files......")

    # send the number of files to server, for int had no encode, cast it to str.
    client_socket.send(str(len(json_list)).encode('UTF-8'))

    print("sending ", len(json_list), "files......")

    for i in range( len(json_list) ):
        file_name = json_list[i]
        print("sending file's name: ", file_name)
        client_socket.send(file_name.encode('UTF-8'))
        with open(file_name, 'r') as fp:
            #cont = fp.read()

            while True:
                cont = fp.read(1024)
                if not cont:
                    break
                while len(cont) > 0:
                    intSent = client_socket.send(cont.encode('UTF-8'))
                    cont = cont[intSent:]
            fp.close()

        #should sleep 3 seconds to avoid some error sending.
        time.sleep(3)
        client_socket.sendall('EOF'.encode('UTF-8'))

    #get another command from client
    order_string = client_socket.recv(1024)
    order_string = order_string.decode('UTF-8')


    #if order_string == "check device":
    device_situation = device_check()
    client_socket.send(device_situation.encode('UTF-8'))
        
    #change work directory back to server.
    #os.chdir(server_dir_path)


        
        

    
    
    
    
    
    
        
   

