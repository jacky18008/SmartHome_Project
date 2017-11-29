ip = $1
username = $2
password = $3

# send and set_path.sh to Client.
sshpass -p '$password' scp set_path.sh $username@$ip:~/Desktop

# run the shell script to make the path.
sshpass -p '$password' ssh $username@$ip 'sh ~/Desktop/set_path.sh'

# send client.py
sshpass -p '$password' scp client.py $username@$ip:'~/Desktop/SmartHome'

#send client_work.sh
sshpass -p '$password' scp client_work.sh $username@$ip:'~/Desktop/SmartHome'

#run
sshpass -p '$password' ssh $username@$ip 'sh ~/Desktop/SmartHome/client_work.sh'

#download client script and run
#wget https://github.com/jacky18008/SmartHome_Project/blob/master/client.py
#python client.py 


