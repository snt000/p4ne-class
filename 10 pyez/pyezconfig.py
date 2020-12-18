from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

pwd = getpass()
ip_addr = input("Enter Juniper IP: ")
ip_addr = ip_addr.strip()

juniper1 = {"host": ip_addr, "user": "steve", "password": pwd}

print ("\n\nConnecting to Juniper...\n")
a_device = Device(**juniper1)
a_device.open()
a_device.timeout = 300

cfg = Config(a_device)
print ("Setting hostname using set notation")
cfg.load("set system host-name j11", format="set", merge=True)
#print "\nSetting hostname using {} notation (external file)"
#cfg.load(path="load_hostname.conf", format="text", merge=True)

print ("Current config differences: ")
print (cfg.diff())

print ("Performing rollback")
cfg.rollback(0)

print ("\nSetting hostname using XML (external file)")
#cfg.load(path="load_hostname.xml", format="xml", merge=True)

cfg.load("set system host-name j222", format="set", merge=True)
print ("Performing commit")
cfg.commit()

