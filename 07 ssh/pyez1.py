from jnpr.junos import Device
from pprint import pprint
device1 = Device(host="192.168.122.71", user="steve",
					passwd="Password")
device1.open()
pprint(device1.facts)
device1.close()

