from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos import Device
device1 = Device(host="10.5.5.4", user="sntuser",
					passwd="Ilovenetworks99")
device1.open()

ports = EthPortTable(device1)
ports.get()
print (type(ports.get()))
print (ports.get())

#for k, v in ports.items():
#    print (k, v)