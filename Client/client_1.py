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
    parser.add_argument('port', metavar='base', type=str,
                        help='Port to the server.')

    #port = int(input("client port?"))

    #parse arguments
    args = parser.parse_args()
    port = int(args.port)

    client_socket.connect(("", port))

    #check if get the port from python subprocess.
    print("get port", port)

    k = ' '
    size = 1024



    #get command from client
    order_string = client_socket.recv(1024)
    order_string = order_string.decode('UTF-8')

    #new device, hasn't sent files
    if order_string == "send files":

        #find all json files and send

        #list it first 
        json_list = []
        import glob, os
        for json_file in glob.glob("*.json"):
            json_list.append(json_file.name)

        # send the number of files to server
        client_socket.send(len(json_list).encode('UTF-8'))

        print("sending ", len(json_list), "files......")

        for i in range( len(json_list) ):
            file_name = json_list[i]
            client_socket.send(name.encode('UTF-8'))
            fp = open(file_name, 'r')
            #cont = fp.read()

            while True:
                cont = fp.read(1024)
                if not cont:
                    break
                while len(cont) > 0:
                    intSent = client_socket.send(cont.encode('UTF-8'))
                    cont = cont[intSent:]

        time.sleep(1)
        client_socket.sendall('EOF'.encode('UTF-8'))

        #get another command from client
        order_string = client_socket.recv(1024)
        order_string = order_string.decode('UTF-8')


    if order_string == "check device":
        device_situation = device_check()
        client_socket.send(device_situation.encode('UTF-8'))


        
        

    
    
    
    
    
    
        
   

