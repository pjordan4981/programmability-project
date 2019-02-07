# programmability-project

Programmabiltiy project to produce a report to show all the devices the have a running config
that has not been saved. I have imported 2 modules, csv and pysnmp, to assist with producing the report.
The input for the program is the DNA Center inventory exported as a csv file.  The program produces
screen output and a file containing all the devices in inventory that have a running configuration that
has not been saved.

The program uses the ccmHistoryRunningLastChanged and ccmHistoryRunningLastSaved
mibs and returns a ticktime value for each mib.  If the ccmHistoryRunningLastChanged ticktime value
is greater than the ccmHistoryRunningLastSaved ticktime value, the configuration has been changed but not saved.
