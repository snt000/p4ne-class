import getpass
import telnetlib

HOST = "10.99.99.7"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)



tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"en\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"term len 0\n") 
#Line above inclded to deal with the More /Spacebar issue .
tn.write(b"show run\n")
tn.write(b"exit\n")

f = open(Hostnames=("r1","r2","r3"),"w")
f.write(tn.read_all().decode('ascii'))
#above line writes all the output from Tn to the text file created in f 
f.close()