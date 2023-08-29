import telnetlib
user="sntuser"
password="Ilovenetworks99"
with open ('router_list.txt','r') as router_file:
    for line in router_file:
        print(line)
        file=open(line.strip("\n"),'w')
        tn=telnetlib.Telnet(line.strip("\n"))
        tn.read_until(b"Username:") 
        tn.write(user.encode('ascii')+b"\n")
        if password:
           tn.read_until(b"Password:")
           tn.write(password.encode('ascii')+b"\n")
        tn.write(b"terminal length 0\n")
        tn.write(b" show configuration\n")
        tn.write(b"exit\n")
        file_var=tn.read_all().decode('ascii')
        file.write(file_var)
    
        file.close()
        print(file_var)
    file.close()