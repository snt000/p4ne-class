from netmiko import ConnectHandler

iosv_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '10.99.99.11',
	'username': 'sntuser',
	'password': 'Ilovenetworks99',
}

net_connect = ConnectHandler(**iosv_l2_s1)
#output = net_connect.send_command('show ip int brief', use_textfsm=True)
#output = net_connect.send_command('show ip route')
output = net_connect.send_command('show ip route', use_textfsm=True)
#output = net_connect.send_command('show ver')
print(output)
print("***********************\n")
#print ("my lovely xxx " + output[0]["serial"][0])
#print (output[0]["serial"])
#for s in output[0]["serial"]:
#    print ("my lovely xxx " + s)

#print("Uptime is " + output[0]["uptime"])

