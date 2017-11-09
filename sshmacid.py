#/usr/bin/python
#IMPORT ALL THE HEAVY LIFTING MODULES THAT DO ALL MY WORK
import sys
import getpass
from netmiko import ConnectHandler
from operator import itemgetter, attrgetter

#INIT
platform = 'cisco_ios'
#host = '10.147.247.232'
#user = 'admin'
pw = getpass.getpass()

#device = ConnectHandler(device_type=platform, ip=host, username=user, password=pw)

devicelist = sys.argv[1]
maclist = sys.argv[2]
user = sys.argv[3]
ofilename = sys.argv[4]

o = open(ofilename,'w')

print "Searching for MAC Patterns: \n"
with open(maclist,'r') as g:
        for item in g:
                print item+'\n'

#ITERATE THROUGH LIST OF SWITCHES CAUSE YEAH
with open(devicelist,'r') as f:
        for ip in f:
        #FOR EVERY SWITCH IN LIST, OPEN SSH
                print "Scanning: " + ip
                output=""
                device = ConnectHandler(device_type=platform, ip=ip, username=user, password=pw)
                #SET TERM LEN TO 0
                device.send_command("term len 0")
                #READ HOSTNAME
                hostname = device.find_prompt()[:-1]
                #CHECK FOR MACS DEFINED IN MAC LIST
                with open(maclist,'r') as g:
                        for item in g:
                                output = output + '\n' + device.send_command("show mac add | i "+item)
                #GTFO AND CLOSE
                device.disconnect()
                #START FORMATTING BY SPLITTING BLOB INTO LINES
                output = output.split('\n')
                #INIT AND DECLARE LISTS
                raw2 = [""]
                #FOR EVERY ITEM IN LIST, CHOP AND SCREW LINES WITH MACS
                #DEPENDING ON FORMAT OF SWITCH
                for item in output:
                        if ("DYNAMIC" in item):
                                raw2.append(item[38:])
                        if ("STATIC" in item):
                                raw2.append(item[38:])
                #SORT AND WRITE TO OUTPUT FILE
                sortout = sorted(raw2)
                o.write( '\n' + hostname + ': ')
                for item in sortout:
                        o.write(item+'\n')
