from nornir import InitNornir
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yml")

rtrs = nr.filter((F(groups__contains="juniper")))

result = rtrs.run(netmiko_send_command, command_string="show version")
print_result(result)

