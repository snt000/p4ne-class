from ncclient import manager
host="10.5.5.4"
with manager.connect(host="10.5.5.4", port=830, 
		username="sntuser", 
                password="Ilovenetworks99",
		device_params={'name':'junos'},
		hostkey_verify=False) as m: 
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)