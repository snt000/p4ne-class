import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.99.99.11', 'sntuser', 'Ilovenetworks99', 120, optional_args={"secret":"cisco"})
iosvl2.open()
 
ios_output = iosvl2.ping("10.99.99.12")
print (json.dumps(ios_output, indent=4))
#ios_output = iosvl2.traceroute(destination="8.8.8.8")
#print (json.dumps(ios_output, indent=4))
iosvl2.close()
