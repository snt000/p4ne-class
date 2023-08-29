from jnpr.junos import Device
from pprint import pprint
device1 = Device(host="10.5.5.4", user="sntuser",
					passwd="Ilovenetworks99")
device1.open()
pprint(device1.facts)
