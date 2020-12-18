import json
from pyntc import ntc_device as NTC
l2=NTC(host="s1", username="steve",password="cisco", device_type="cisco_ios_ssh")
l2.open()
l2.reboot(confirm=True)
l2.close()
