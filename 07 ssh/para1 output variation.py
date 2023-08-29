import paramiko
import time
import json

ip_address = "10.99.99.11"
username = "sntuser"
password = "Ilovenetworks99"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password,look_for_keys=False)
print ("Successful connection", ip_address)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("sh ip int brief\n")

time.sleep(1)
output = remote_connection.recv(65535)
print (output)
print("************************\n")
o = str(output)
print (o.replace(r'\r\n', '\n'))

ssh_client.close()