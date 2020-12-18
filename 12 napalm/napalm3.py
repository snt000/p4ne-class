import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.3', 'steve', 'cisco')
iosvl2.open()
 
ios_output = iosvl2.ping("192.168.122.1")
print (json.dumps(ios_output, indent=4))
ios_output = iosvl2.traceroute(destination="8.8.8.8")
print (json.dumps(ios_output, indent=4))
iosvl2.close()
