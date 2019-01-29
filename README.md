# programmability-project
create a program to parse a CSV file and print the status of the running config of a devive
programmabiltiy project to produce a report to show all the devices the have a running config that has not been savedted

I have imported 2 modules to assist with producing a report that lists all the devices in inventory that has a running-config that has not been saved. This is phase one where the current code produce a print of of the snmp query of the snmp mibs ccmHistoryRunningLastChanged and ccmHistoryRunningLastSaved.

If the value of ccmHistoryRunningLastChanged is greater than ccmHistoryRunningLastSaved, the configuration has been changed but not saved."
