from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nr = InitNornir("config.yml")

print ("Lists of all hosts in inventory:")
print (nr.inventory.hosts)