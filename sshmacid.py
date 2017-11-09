#/usr/bin/python
#IMPORT ALL THE HEAVY LIFTING MODULES THAT DO ALL MY WORK
import sys
import getpass
from netmiko import ConnectHandler
from operator import itemgetter, attrgetter

#INIT NETMIKO CONNECTHANDLER STRINGS
platform = 'cisco_ios'
pw = getpass.getpass()

#SAVE ARGS TO VARS CAUSE WHY NOT
devicelist = sys.argv[1]
maclist = sys.argv[2]
user = sys.argv[3]
ofilename = sys.argv[4]

#OPEN OUTPUT FILE
o = open(ofilename,'w')

#TELL CONSOLE USER WHICH MACS ARE BEING SEARCHED FOR
print "Searching for MAC Patterns: \n"
with open(maclist,'r') as g:
        for item in g:
                print item+'\n'

#OPEN LIST OF SWITCHES, ITERATE THROUGH AND DO WORK
with open(devicelist,'r') as f:
        for ip in f:
        #FOR EVERY SWITCH IN LIST, OPEN SSH
                #INFORM CONSOLE USER WTF IS GOING ON
                print "Scanning: " + ip
                #INIT OUTPUT VARIABLE
                output=""
                
                #INIT AND CONNECT NETMIKO DEVICE
                device = ConnectHandler(device_type=platform, ip=ip, username=user, password=pw)
                
                #SET TERM LEN TO 0
                device.send_command("term len 0")
                
                #READ HOSTNAME
                hostname = device.find_prompt()[:-1]
                
                #CHECK CURRENT SWITCH FOR MACS DEFINED IN MAC LIST
                with open(maclist,'r') as g:
                        for item in g:
                                output = output + '\n' + device.send_command("show mac add | i "+item)
                
                #GTFO AND CLOSE
                device.disconnect()
                
                #START FORMATTING BY SPLITTING BLOB INTO LINES
                output = output.split('\n')
                
                #INIT AND DECLARE OUTPUT LIST
                raw2 = [""]
                
                #SEARCH FOR MACS IN CISCO WAY OF DOING THINGS
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
#SAY YOU'RE DONE
print "Scan complete"
