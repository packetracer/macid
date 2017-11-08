#/usr/bin/python
#IMPORT ALL THE HEAVY LIFTING MODULES THAT DO ALL MY WORK
import sys
import telnetlib
from operator import itemgetter, attrgetter

#INIT PASSWORD, DEFINE YO PASSWORD HERE
password = ""

#ITERATE THROUGH LIST OF SWITCHES CAUSE YEAH
with open('switches.list','r') as f:
        for ip in f:
        #FOR EVERY SWITCH IN LIST, OPEN TELNET
                tn = telnetlib.Telnet(ip)
                #LOGIN TO SWITCH
                tn.read_until("Password: ")
                tn.write(password + "\n")
                tn.write("en" + "\n")
                tn.read_until("Password: ")
                tn.write(password + "\n")
                #SET TERM LEN TO 0
                tn.write("term len 0\n")
                #READ HOSTNAME
                hostname = tn.read_until("#")[:-1]
                #CHECK FOR MACS OF ZERO CLIENTS- WILL CHANGE IN FUTURE VERSION
                tn.write("show mac add | i 5cf6\n")
                tn.write("show mac add | i cc2d\n")
                #GTFO AND CLOSE
                tn.write("exit\n")
                tn.write("exit\n")
                raw = tn.read_all()
                tn.close()
                #START FORMATTING BY SPLITTING BLOB INTO LINES
                raw = raw.split('\r\n')
                #INIT AND DECLARE LISTS
                raw2 = [""]
