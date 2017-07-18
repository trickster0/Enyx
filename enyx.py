#!/usr/bin/python
import subprocess
import sys
import os
import os.path
print '''###################################################################################
#                                                                                 #
#                      #######     ##      #  #    #  #    #                      #
#                      #          #  #    #    #  #    #  #                       #
#                      ######    #   #   #      ##      ##                        #
#                      #        #    # #        ##     #  #                       #
#                      ######  #     ##         ##    #    #                      #
#                                                                                 #
#                           SNMP IPv6 Enumerator Tool                             #
#                                                                                 #
#                   Author: Thanasis Tserpelis aka Trickster0                     #
#                                                                                 #
###################################################################################
\r\n'''
if len(sys.argv)<2:
	print "[+] Usage: " + str(sys.argv[0]) + " IP"
	print "[+] Input an IP"	
	sys.exit()
if os.path.isfile("/usr/bin/snmpwalk"):
    print "[+] Snmpwalk found."
    print "[+] Grabbing IPv6."
    ip=str(sys.argv[1])
    command = 'snmpwalk -c public -v 2c ' + ip + ' | grep "3.6.1.2.1.4.34.1.3.2.16"|cut -d "." -f 13-28 | cut -d " " -f 1'
    p=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = p.communicate()[0]
#splitting each ip
    IPS=output.split("\n")
#separating each ip in arrays
    first=IPS[0]
    second=IPS[1]
    third=IPS[2]
#joining the arrays to strigns
    stringone=''.join(first)
    stringtwo=''.join(second)
    stringthree=''.join(third)
#splitting the . between the strigns and making the from str>int>hex
    list1=stringone.split(".")
    integer1=map(int,list1)
    hex1=map(hex,integer1)
    list2=stringtwo.split(".")
    integer2=map(int,list2)
    hex2=map(hex,integer2)
    list3=stringthree.split(".")
    integer3=map(int,list3)
    hex3=map(hex,integer3)
#Removing 0x from all the inputs in the arrays
    s=0
    for j in hex3:
    	    hex3[s]=j.replace("0x","")
	    s=s+1
    s=0
    for h in hex2:
            hex2[s]=h.replace("0x","")
            s=s+1
    s=0
    for k in hex1:
            hex1[s]=k.replace("0x","")
            s=s+1

#Creating doubles for inputs in arrays that are less than 2 digits aka 0x
    s=0
    mystring="0"
    for l in hex3:
	    if len(hex3[s])<2:
		    hex3[s]=mystring+l
	    s=s+1
    s=0
    mystring="0"
    for z in hex2:
            if len(hex2[s])<2:
                    hex2[s]=mystring+z
            s=s+1
    s=0
    mystring="0"
    for y in hex1:
            if len(hex1[s])<2:
                    hex1[s]=mystring+y
            s=s+1
#joining the arrays
    almost1=''.join(hex1)
    almost2=''.join(hex2)
    almost3=''.join(hex3)
#adding : in the ip strigns
    final1=almost1[:4] + ":" + almost1[4:8] + ":" + almost1[8:12] + ":" + almost1[12:16] + ":" + almost1[16:20] + ":" + almost1[20:24] + ":" + almost1[24:28] + ":" + almost1[28:32]
    final2=almost2[:4] + ":" + almost2[4:8] + ":" + almost2[8:12] + ":" + almost2[12:16] + ":" + almost2[16:20] + ":" + almost2[20:24] + ":" + almost2[24:28] + ":" + almost2[28:32]
    final3=almost3[:4] + ":" + almost3[4:8] + ":" + almost3[8:12] + ":" + almost3[12:16] + ":" + almost3[16:20] + ":" + almost3[20:24] + ":" + almost3[24:28] + ":" + almost3[28:32]
    print "[+] Here They Come...\r\n"
    print "[+] Loopback -> " + " " + final1
    print "[+] Unique Local -> " + " " + final2
    print "[+] Link-Local -> " + " " + final3
else:
    print "[X] Please Install snmpwalk!"
    print "[*] sudo apt-get install snmp"
    sys.exit()
