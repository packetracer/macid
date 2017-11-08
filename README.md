# macid
Identifies ports that match specific MAC address
macid = SPECIFIC TO TELNET.  SORRY I KNOW ROFL RIGHT?
sshmacid = SSH based

Takes input of a textfile and username
textfile should not have any empty lines, should only include valid IPv4 addresses or you'll explode the script


usage:
python sshmacid.py <switchesfile> <username>
  
so for instance

python sshmacid.py switches.list admin
