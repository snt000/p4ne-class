from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="config.yml")

result = nr.run(netmiko_send_command, command_string="sh ip int brief")
print_result(result)

