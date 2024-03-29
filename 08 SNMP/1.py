from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('10.99.99.11',161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex)-1][0]or'?'))
else:
    for varBind in varBinds:
        print('='.join([x.prettyPrint() for x in varBind]))