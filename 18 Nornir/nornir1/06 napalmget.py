from nornir import InitNornir
#Below no longer needed
#from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli

nr = InitNornir("config.yml")

r = nr.filter(name="devxe1")

result = r.run(napalm_cli, commands=["sh ver", "sh ip int brief"])
print_result(result)

