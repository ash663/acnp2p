import os
import socket

#we receive peer-hostname and peer-portnumber

# TODO: Write code to accept cmd line args

peerHostname='abcd'
peerPort=1234
#peers is a list of peerTuples. Add code to extract data from an external file 'peers'/'peers.csv'
peers = []
#sample dns. Addressed by peerHostname
dns = {'abcd':'10.0.0.1', 'xyz':'10.0.0.2'}

if peerHostname in dns.keys():
    peerIP = dns[peerHostname]
    ping = os.system("ping -c 1 " + peerIP)

    if ping==0:
        #peer exists
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((peerIP, peerPort))
        if result==0:
            #we gucci
            peerTuple = (peerHostname, peerIP, peerPort)
            if peerTuple in peers:
                #Duplicate
                continue
            else:
                #add tuple to existing peers
                peers.append(peerTuple)
        else:
            #problem!
    else:
        continue
