import json
from pyntc import ntc_device as NTC
l2=NTC(host="10.99.99.10", username="cisco",password="cisco", secret="cisco", device_type="cisco_ios_ssh")
l2.open()
f=l2.facts
print(json.dumps(f,indent=4))
l2.close()
