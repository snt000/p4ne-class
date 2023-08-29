import getpass
import telnetlib

HOST = "10.99.99.7"
user = input("Enter your remote account: ")
password = getpass.getpass()
i=0
hostname = ["r1.cfg", "r2.cfg", "s3.cfg"]

for HOST in ["10.99.99.7","10.99.99.10","10.99.99.15"]:

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

    f = open(hostname[i],"w")
    #f2 = open(hostname[2],"w")
    #tn.read_until(b"upgrade fpd auto")
    f.write(tn.read_all().decode('ascii'))
    #above line writes all the output from Tn to the text file created in f 
    f.close()
    i+=1

