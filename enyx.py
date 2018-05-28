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
if len(sys.argv)<4:
	print "[+] Usage: " + str(sys.argv[0]) + " snmpversion communitystring IP"
	print "[+] snmpversion can be either 1 or 2c\r\n"
	sys.exit()
if os.path.isfile("/usr/bin/snmpwalk"):
	print "[+] Snmpwalk found."
	ip=str(sys.argv[3])
	version=str(sys.argv[1])
	community=str(sys.argv[2])
	command = 'snmpwalk -c ' + community + ' -v ' + version + ' '  + ip + ' iso.3.6.1.2.1.4.34.1.3.2.16|cut -d "." -f 13-28 | cut -d " " -f 1'
	p=subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
	output = p.communicate()[0]
	IPS=output.split("\n")
	output2 = len(IPS)-1
	def ip(IPS):
		for i in range(0,output2):
			step1=IPS[i]
			step2=''.join(step1)
			step3=step2.split(".")
			step4=map(int,step3)
			step5=map(hex,step4)
			s=0
			for j in step5:
				step5[s]=j.replace("0x","")
				s=s+1
			s=0
			step6="0"
			for l in step5:
				if len(step5[s])<2:
					step5[s]=step6+l
				s=s+1
			step7=''.join(step5)
			step8=step7[:4] + ":" + step7[4:8] + ":" + step7[8:12] + ":" + step7[12:16] + ":" + step7[16:20] + ":" + step7[20:24] + ":" + step7[24:28] + ":" + step7[28:32]
			sentences=["[+] Loopback -> ","[+] Link Local -> ","[+] Unique-Local -> "]
			if step7[:4]=="fe80":
				print sentences[1] + step8
			elif step7[:4]=="0000":
				print sentences[0] + step8
			else:
				print sentences[2] + step8

	if output2 == 1:
		print "[X] No IPv6 IP Found."
	else:
		print "[+] Grabbing IPv6."
		ip(IPS)
