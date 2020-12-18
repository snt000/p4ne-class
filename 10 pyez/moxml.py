from ncclient import manager
host="10.2.2.2"
with manager.connect(host="10.2.2.2", port=830, 
		username="moyaze", 
                password="Cisco123",
		device_params={'name':'junos'},
		hostkey_verify=False) as m: 
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)

