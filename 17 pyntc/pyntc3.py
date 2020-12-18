import json
from pyntc import ntc_device as NTC
l2=NTC(host="192.168.122.3", username="steve",password="cisco", device_type="cisco_ios_ssh")
l2.open()
o=l2.show("show run")
print o
l2.close()
