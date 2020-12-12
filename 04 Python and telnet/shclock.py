import getpass
import telnetlib

HOST = "10.99.99.10"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"sh clock\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))