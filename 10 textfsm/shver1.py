import ntc_templates
from netmiko import ConnectHandler

mytarget = {
	'device_type': 'cisco_ios',
	'ip': '10.99.99.10',
	'username': 'cisco',
	'password': 'cisco',
    'secret': 'cisco'
}

nc = ConnectHandler(**mytarget)
output = nc.send_command('show ver')
print("Plain text output")
print(output)
print("Structured data")
output = nc.send_command('show ip int', use_textfsm=True)
print(output)