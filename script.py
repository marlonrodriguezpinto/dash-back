
from scapy.all import *
import time
text_file = open("Output.txt", "w")


def arp_display(pkt):

    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc=='44:65:0d:4a:af:e2':
            print "pushed PLAY DOUGH dash button with a mac address of: " + pkt[ARP].hwsrc
            text_file.write("%s\n" % pkt[ARP].hwsrc)
        else:
            print "ARP Probe from unknown device:" + pkt[ARP].hwsrc	
	
print sniff(prn=arp_display, filter="arp", store=0, count=0)
text_file.close()


