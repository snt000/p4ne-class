import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.99.99.11', 'sntuser', 'Ilovenetworks99', optional_args={"secret":"cisco"})
iosvl2.open()
 
#ios_output = iosvl2.get_mac_address_table()
ios_output = (iosvl2.get_config())
#print(type(ios_output))

#Note ios_output is a dict with three? keys - startup, running, candidate
#ios_output = iosvl2.get_firewall_policies()

#print ((json.dumps(ios_output, indent=4)))
#print ((json.dumps(ios_output, indent=4)).replace(r'\n', '\n'))
#print ((json.dumps(ios_output["running"], indent=4)).replace(r'\n', '\n'))
#print ((json.dumps(ios_output, indent=4)).splitlines())
#print (ios_output)
print (ios_output["running"])
iosvl2.close()
