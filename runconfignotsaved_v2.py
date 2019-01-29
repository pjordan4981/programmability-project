from pysnmp.hlapi import *
import os
import csv


with open('/usr/local/bin/snmp/test.csv', newline='') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        name = (row[1])
        ipadder = (row[2])
        #print (name, ipadder)


    for (errorIndication,
        errorStatus,
        errorIndex,
        varBinds) in getCmd(SnmpEngine(),
                    CommunityData('secmob-2c', mpModel=0),
                    UdpTransportTarget((ipadder, 161)),
                    ContextData(),
                    ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.43.1.1.1.0'))):

        if errorIndication or errorStatus:
                print(errorIndication or errorStatus)
                break
        else:
            for varBind in varBinds:
                continue
                #print(' = '.join([x.prettyPrint() for x in varBind]))


    for (errorIndication,
        errorStatus,
        errorIndex,
        varBinds) in getCmd(SnmpEngine(),
                    CommunityData('secmob-2c', mpModel=0),
                    UdpTransportTarget((ipadder, 161)),
                    ContextData(),
                    ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.43.1.1.2.0'))):
        if errorIndication or errorStatus:
            print(errorIndication or errorStatus)
            break
        else:
            for varBind1 in varBinds:
                #print(' = '.join([x.prettyPrint() for x in varBind1]))

                #print ('Runnig-config last changed', varBind)
                #print ('Runnig-config last saved', varBind1)

                tickssaved = str(varBind)
                tickssaved = tickssaved.split('= ')[1]
                tickschanged = str(varBind1)
                tickschanged = tickschanged.split('= ')[1]
        if tickssaved < tickschanged:
            print ('\n\n',name, ' is compliant.','\n\n')
        else:
            print ('\n\n',name, 'host is not compliant.','\n\n')

        #int_tickssaved = int(tickssaved)
                #tickschanged = varBind1.split('= ')[1]
        # intitially this didn't appear to work as text so I conveted to an integer
        #currently seams to be working as text
        #int_tickschanged = int(tickschanged)
        #print (tickssaved < tickschanged)
#print ('If the value of ccmHistoryRunningLastChanged is greater than ccmHistoryRunningLastSaved, the configuration has been changed but not saved for host',name,'. The host ip address is', ipadder,'.')
csvFile.close()



        #file = csv.reader(open('file.csv'), delimiter=',')
