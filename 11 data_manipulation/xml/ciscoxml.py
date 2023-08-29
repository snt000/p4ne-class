import xmltodict
from pprint import pprint

# Open the sample xml file and read it into variable
with open("sandbox.xml") as f:
    xml_example = f.read()

# Print the raw XML data
#print(xml_example)

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)

#for item in xml_dict.items():
#  pprint (item)

#for k,v in xml_dict.items():
#  if type(v) is dict:
#    pprint (v)

def finditem(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = finditem(v, key)
            if item is not None:
                return item

print (finditem (xml_dict, "interfaces"))

# Revert to the XML string version of the dictionary
#print(xmltodict.unparse(xml_dict))