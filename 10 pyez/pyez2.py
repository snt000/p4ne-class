from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.op.ethport import EthPortTable

device1 = Device(host="10.5.5.4", user="sntuser",
					passwd="Ilovenetworks99")
device1.open()
#pprint(device1.facts)
ports=EthPortTable(device1)
ports.get()

print (ports)

#for k, v in ports["ge-0/0/0"].items():
#	print (k, v)