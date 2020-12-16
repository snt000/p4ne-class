import getpass
import telnetlib

HOST = "10.99.99.10"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
f = open ("r1.cfg", "w")

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal length 0\n")
tn.write(b"sh run\n")
tn.write(b"exit\n")

f.write(tn.read_all().decode('ascii'))
#print(tn.read_all().decode('ascii'))
f.close()