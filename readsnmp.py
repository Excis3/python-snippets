#!/usr/bin/python
import netsnmp      # SNMP library

HOST = ''           # Host to read snmp
RW_STRING = ''      # community string (password)
OID = ''            # OID value

session = netsnmp.Session(DestHost=HOST, Version=1, Community=RW_STRING)
vars1 = netsnmp.VarList(netsnmp.Varbind(OID))

result = str(session.get(vars1))
result = result[2:]
oidvalue = result[:-3]

print(oidvalue)
