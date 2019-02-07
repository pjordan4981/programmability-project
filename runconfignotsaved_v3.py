"""
Programmabiltiy project to produce a report to show all the devices the have a running config
that has not been saved. I have imported 2 modules, csv and pysnmp, to assist with producing the report.
The input for the program is the DNA Center inventory exported as a csv file.  The program produces
screen output and a file containing all the devices in inventory that have a running configuration that
has not been saved.

The program uses the ccmHistoryRunningLastChanged and ccmHistoryRunningLastSaved
mibs and returns a ticktime value for each mib.  If the ccmHistoryRunningLastChanged ticktime value
is greater than the ccmHistoryRunningLastSaved ticktime value, the configuration has been changed but not saved.
"""

from pysnmp.hlapi import *
import csv
import os
import datetime
#import time

from datetime import date


def get_fn_datetime():
    # Use current date to get a text file name.
    return "configs-not-saved-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"

# Get full path for writing.
not_saved_devices = get_fn_datetime()

#print(not_saved_devices)


with open('test.csv') as csvFile:
    reader = csv.DictReader(csvFile)
    for dct in map(dict, reader):
        #print(f"{dct['Device Name']} {dct['IP Address']}")



        running = getCmd(SnmpEngine(),
                    CommunityData('secmob-2c', mpModel=0),
                    #UdpTransportTarget((ipadder, 161)),
                    UdpTransportTarget((dct['IP Address'], 161)),
                    ContextData(),
                    ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.43.1.1.1.0')))

        # this is what you get from SNMP agent
        error_indication, error_status, error_index, var_binds = next(running)

        if not error_indication and not error_status:
        # each element in this list matches a sequence of `ObjectType`
        # in your request.
        # In the code above you requested just a single `ObjectType`,
        # thus we are taking just the first element from response
            oid, value = var_binds[0]

        saved = getCmd(SnmpEngine(),
                CommunityData('secmob-2c', mpModel=0),
                #UdpTransportTarget((ipadder, 161)),
                UdpTransportTarget((dct['IP Address'], 161)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.43.1.1.2.0')))
        # this is what you get from SNMP agent
        error_indication, error_status, error_index, var_binds = next(saved)

        if not error_indication and not error_status:
        # each element in this list matches a sequence of `ObjectType`
        # in your request.
        # In the code above you requested just a single `ObjectType`,
        # thus we are taking just the first element from response
            oid, value2 = var_binds[0]


        #print(dct['Device Name'],dct['IP Address'],'Runnig-config last changed', '=', value)
        #print(dct['Device Name'],dct['IP Address'],'Runnig-config last saved', '=', value2)

        if value > value2:
            print('\n','The configuration has been changed but not saved for host,', dct['Device Name'],dct['IP Address'])
            #with open('not_saved_devices.csv', 'w', newline='') as csvfile:
                #spamwriter = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                #spamwriter.writerow(dct['Device Name'])

            with open(not_saved_devices, 'a', newline='') as csvfile:
                fieldnames = ('Device Name', 'IP Address')
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Device Name': dct['Device Name'], 'IP Address': dct['IP Address']})


        #else:
        #    print ('The configuration has been saved for host,', dct['Device Name'],dct['IP Address'])


csvFile.close()
