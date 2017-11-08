#/usr/bin/python
#IMPORT ALL THE HEAVY LIFTING MODULES THAT DO ALL MY WORK
import sys
import getpass
from netmiko import ConnectHandler
from operator import itemgetter, attrgetter

#INIT
platform = 'cisco_ios'
pw = getpass.getpass()

#device = ConnectHandler(device_type=platform, ip=host, username=user, password=pw)

devicelist = sys.argv[1]
user = sys.argv[2]
#ITERATE THROUGH LIST OF SWITCHES CAUSE YEAH
with open(devicelist,'r') as f:
        for ip in f:
        #FOR EVERY SWITCH IN LIST, OPEN SSH
                output=""
                output2=""
                device = ConnectHandler(device_type=platform, ip=ip, username=user, password=pw)
                #SET TERM LEN TO 0
                device.send_command("term len 0")
                #READ HOSTNAME
                hostname = device.find_prompt()
                #CHECK FOR MACS OF ZERO CLIENTS- WILL CHANGE IN FUTURE VERSION
                output = device.send_command("show mac add | i 5cf6")
                output2 = device.send_command("show mac add | i cc2d")
                #GTFO AND CLOSE
                device.disconnect()
                #START FORMATTING BY SPLITTING BLOB INTO LINES
                output = output+'\n'+output2
                output = output.split('\n')
                #INIT AND DECLARE LISTS
                raw2 = [""]
                #FOR EVERY ITEM IN LIST, CHOP AND SCREW LINES WITH MACS
                #DEPENDING ON FORMAT OF SWITCH
                for item in output:
                        #print "ITEM = " + item
                        if ("DYNAMIC" in item):
                                raw2.append(item[38:])
                        if ("STATIC" in item):
                                raw2.append(item[38:])
                #SORT AND PRINT
                sortout = sorted(raw2)
                print '\n' + hostname + ': '
                for item in sortout:
                        print item
