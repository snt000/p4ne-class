from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in bulkCmd(SnmpEngine(),
                          UsmUserData('usr-none-none'),
                          UdpTransportTarget(('demo.snmplabs.com', 161)),
                          ContextData(),
                          0, 50,
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'system')),
                          maxCalls=10):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
