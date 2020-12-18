import json
from napalm import get_network_driver
driver = get_network_driver('ios')
l2 = driver('10.99.99.7', 'cisco', 'cisco', optional_args={"secret": "cisco"})
l2.open()
 
ios_output = l2.get_facts()
#Doesnt look nice
print (ios_output) 
#print (json.dumps(ios_output, indent=4))
l2.close()
