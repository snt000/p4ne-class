import paramiko
import time

#ip_address = "10.99.99.11"
#username = "sntuser"
#password = "Ilovenetworks99"
d={
    "hostname":"10.99.99.11",
    "username":"sntuser",
    "password":"Ilovenetworks99",
    "look_for_keys": False}

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh_client.connect(hostname=ip_address,username=username,password=password,look_for_keys=False)
ssh_client.connect(**d)
#print ("Successful connection", ip_address)
print ("Successful connection", d["hostname"])

remote_connection = ssh_client.invoke_shell()
#remote_connection.send("sh ip int brief\n")

remote_connection.send("configure terminal\n")

for n in range (2,21):
    print ("Creating VLAN " + str(n))
    remote_connection.send("vlan " + str(n) +  "\n")
    remote_connection.send("name snt" + str(n) +  "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print (output)

ssh_client.close()

