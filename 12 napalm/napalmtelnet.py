import json
from napalm import get_network_driver
driver = get_network_driver('ios')
l2 = driver('10.99.99.44', 'sntuser', 'Ilovenetworks99', 
            optional_args={"secret": "cisco", "port":23, "transport": "telnet"})
l2.open()
 
ios_output = l2.get_facts()
#Doesnt look nice
print ("NOT NICE\n")
print (ios_output) 
print ("\nNICE\n")
print (json.dumps(ios_output, indent=4))
l2.close()
