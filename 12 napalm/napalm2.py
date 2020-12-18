import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.99.99.10', 'cisco', 'cisco', optional_args={"secret":"cisco"})
iosvl2.open()
 
#ios_output = iosvl2.get_mac_address_table()
ios_output = iosvl2.get_config()
#Note ios_output is a dict with three? keys - startup, running, candidate
#ios_output = iosvl2.get_firewall_policies()
print (json.dumps(ios_output, indent=4))
#print (ios_output)
iosvl2.close()
