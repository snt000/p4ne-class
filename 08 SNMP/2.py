from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('10.99.99.11',161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0)))
)
