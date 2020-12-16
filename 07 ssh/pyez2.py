from jnpr.junos import Device
from pprint import pprint
device1 = Device(host="192.168.122.71", user="steve",
					passwd="Password")
device1.open()
#pprint(device1.facts)
from jnpr.junos.op.ethport import EthPortTable
ports = EthPortTable(device1)
ports.get()

for k, v in ports["ge-0/0/0"].items():
    print k, v
