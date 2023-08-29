from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.utils.config import Config
j1 = Device(host="10.5.5.4", user="steve",
					passwd="Ilovenetworks99")
j1.open()
cfg = Config(j1)
cfg.load(path="/root/wednesday/10.2.2.2.xml", format="xml", overwrite=True)
cfg.commit()
