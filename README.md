# macid/sshmacid
Identifies ports that match specific MAC address

macid = SPECIFIC TO TELNET.  SORRY I KNOW ROFL RIGHT?

sshmacid = SSH based

Takes input of a textfile and username
textfile should not have any empty lines, should only include valid IPv4 addresses or you'll explode the script

Checks for existence of LG and Samsung Zero clients connected to switches (based on OUI).  next version will allow you to input patterns of MAC addresses (coming soon)

usage:
python sshmacid.py <switchesfile> <username>
  
so for instance

python sshmacid.py switches.list admin
