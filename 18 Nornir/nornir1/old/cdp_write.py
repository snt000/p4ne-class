
from nornir import InitNornir
#from nornir.plugins.functions.text import print_result, print_title
from nornir_utils.plugins.functions import print_result
#from nornir.plugins.tasks.networking import netmiko_send_command, netmiko_send_config
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir.core.filter import F

nr = InitNornir(config_file="config.yml")
rtrs = nr.filter((F(groups__contains="iosv")))

def cdp_map(task):
    #r = task.run(task=netmiko_send_command, command_string = "show cdp neighbor", use_genie=True)
    r = task.run(task=netmiko_send_command, command_string = "show cdp neighbor")
    task.host["facts"] = r.result
    outer = task.host["facts"]
    print (outer)
    indexer = outer['cdp']['index']
    for idx in indexer:
        local_intf = indexer[idx]['local_interface']
        remote_port = indexer[idx]['port_id']
        remote_id = indexer[idx]['device_id']
        stripname = remote_id.split(".")
        cdp_config = task.run(netmiko_send_config,name="Automating CDP Network Descriptions",config_commands=[
            "interface " + str(local_intf),
            "description Connected to " + str(stripname[0]) + " via Gi" + str(remote_port)]
        )



results = rtrs.run(task=cdp_map)
print_result(results)