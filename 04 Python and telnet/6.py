import telnetlib
user="sntuser"
password="Ilovenetworks99"

with open("h.txt", "r") as router_file:
    
    for line in router_file:
        print(line)

        tn = telnetlib.Telnet(line.strip("\n"))
        
        tn.read_until(b"Username:")
        tn.write(user.encode("ascii") + b"\n")

        if password:
            tn.read_until(b"Password:")
            tn.write(password.encode("ascii") + b"\n")


        #tn.write(b"enable\n")
        #tn.write(b"cisco\n")
        tn.write(b"terminal length 0\n")
        tn.write(b"sh run\n")
        tn.write(b"exit\n")

        #print(tn.read_all().decode('ascii'))

        f = open(f"new-{line.strip()}.txt", "w")

        f.write(tn.read_all().decode('ascii'))