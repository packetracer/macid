#sshmacid

Main use: Identifies ports that match specific MAC address on a switch.

Detailed usae: Takes input of a textfile and username
textfile should not have any empty lines, should only include valid IPv4 addresses or you'll explode the script
Uses file with list of IPs and file with list of MACs to find those MACs in those switches.  Outputs results to a user defined text file with ***somewhat*** sorted port numbers.  

Example "switch text file":

<---Begin File--->

10.0.0.1

10.0.0.2

10.0.0.3

10.0.0.4

10.0.0.5

<---End File--->

Example "mac text file"

<---Begin File--->

cc2d

14cd.13

<---End File--->

*NOTE DO NOT PUT THE SHIT IN THE <-- ---> IN YOUR TEXT FILE, THIS IS JUST TO SHOW THE BEGINING AND END OF A TEXT FILE.  

usage:
python sshmacid.py switchesfile maclist username outputfile
  
so for instance:
python sshmacid.py switches.list MAC.txt admin zeroclients.txt

At combat speed:
--------------------------
lghnixadm@svrmgt05:~/py/UHC$ sudo python sshmac2.py switches.list MAC.txt rjp zero

Password:

Searching for MAC Patterns:

14c9.13


cc2d


Scanning: 10.147.15.1

Scanning: 10.147.16.1

Scanning: 10.147.17.1

Scanning: 10.147.18.1

Scanning: 10.147.19.1

Scan complete
lghnixadm@svrmgt05:~/py/UHC$ cat zero

LGH_4th_Floor_Main:
Gi1/0/10

Gi1/0/11

Gi1/0/12

Gi1/0/18

Gi1/0/2

Gi1/0/34

Gi1/0/37

Gi1/0/38

Gi1/0/4

Gi1/0/42

Gi1/0/6


LGH_4th_Floor_West:
Gi1/0/2

Gi2/0/15

Gi2/0/32

Gi2/0/33

Gi2/0/34

Gi2/0/35

Gi2/0/37

Gi2/0/38

Gi2/0/40


LGH_5th_Floor_Main:

Gi1/0/14

Gi1/0/16

Gi1/0/25

Gi1/0/27

Gi1/0/28

Gi1/0/29

Gi1/0/33

Gi1/0/39

Gi1/0/41

Gi1/0/42

Gi1/0/43

Gi1/0/5


LGH_5th_Floor_West:

Gi1/0/12

Gi1/0/21

Gi1/0/28

Gi1/0/4

Gi1/0/9

Gi2/0/15

Gi2/0/19

Gi2/0/20

Gi2/0/21

Gi2/0/26

Gi2/0/27

Gi2/0/37

Gi2/0/39

Gi2/0/44

Gi3/0/19

Gi3/0/21

Gi3/0/22

Gi3/0/25

Gi3/0/26

Gi3/0/28

Gi3/0/33

Gi3/0/42

Gi3/0/44

Gi3/0/45


LGH_6th_Floor_Main:

Gi1/0/10

Gi1/0/11

Gi1/0/13

Gi1/0/16

Gi1/0/33

Gi1/0/34

Gi1/0/37

Gi1/0/38

Gi1/0/4

Gi1/0/42

Gi1/0/5

Gi1/0/7

Gi1/0/9

Gi2/0/42

Gi2/0/43

Gi2/0/6

Gi2/0/7

------------

TADA

![alt text](https://vignette.wikia.nocookie.net/looneytunes/images/e/e1/All.jpg/revision/latest/scale-to-width-down/260?cb=20150313020828)
