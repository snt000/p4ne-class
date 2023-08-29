import getpass
import telnetlib
user = "sntuser"
password = "Ilovenetworks99"
for n in range (1,5):
    host = "10.99.99.1"
    full_host = host + str(n)
    tn = telnetlib.Telnet(full_host)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    data = tn.read_all().decode('ascii')
    fileName = full_host + ".txt"
    print(fileName)
    with open(fileName, 'w+') as f:
        f.write(data)
        #f.close()