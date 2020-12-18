import json
from pyntc import ntc_device as NTC
l2=NTC(host="s1", username="steve",password="cisco", device_type="cisco_ios_ssh")
l2.open()
l2.config_list(["hostname s1",
		"router ospf 1",
		"network 0.0.0.0 255.255.255.255 area 0",
		"end"])
l2.close()
