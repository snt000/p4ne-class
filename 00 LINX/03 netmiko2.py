from netmiko import ConnectHandler

l2 = {
    'device_type': 'cisco_ios', 'ip': '10.99.99.11', 'username': 'sntuser', 'password': 'Ilovenetworks99', 'secret': 'cisco' }

net_connect = ConnectHandler(**l2)
output = net_connect.send_command('show ip int brief')
print (output)

net_connect.enable()

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)



