from nornir import InitNornir
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

nr = InitNornir("config.yml")

d = "Interface description set by nornir"
#The f below is an f string - d is placed in the string
dconfig = [ "interface gi0/0", f"description {d}", ]

rtrs = nr.filter((F(groups__contains="iosv")))

result = rtrs.run(netmiko_send_config, config_commands=dconfig)
print_result(result)

