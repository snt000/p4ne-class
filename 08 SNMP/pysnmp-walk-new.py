import asyncio
from pysnmp.hlapi.v3arch.asyncio import *

async def run():
    snmpEngine = SnmpEngine()

    asyncGen = walk_cmd(
        snmpEngine,
        CommunityData("public", mpModel=0),
        await UdpTransportTarget.create(("demo.pysnmp.com", 161)),
        ContextData(),
        ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2")),
    )
    
    async for myTuple in asyncGen:
        errorIndication, errorStatus, errorIndex, varBinds = myTuple
        if errorIndication:
                print(errorIndication)

        elif errorStatus:
            print(
                "{} at {}".format(
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
                )
            )
        else:
            for varBind in varBinds:
                print(" = ".join([x.prettyPrint() for x in varBind]))

asyncio.run(run())