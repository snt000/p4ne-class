from ncclient import manager
import xmltodict

with manager.connect(host="10.5.5.4", port=830,
								username="sntuser",
								hostkey_verify=False,
                                password="Ilovenetworks99",
								device_params={'name':'junos'}) as m:
    c = m.get_config(source='running').data_xml
    with open("10.5.5.4.xml", 'w') as f:
        f.write(c)
    
    with open("10.5.5.4.xml") as f:
        xml_example = f.read()

        # Print the raw XML data
        print(xml_example)

        # Parse the XML into a Python dictionary
        xml_dict = xmltodict.parse(xml_example)

        print (xml_dict)

        print(xmltodict.unparse(xml_dict))

