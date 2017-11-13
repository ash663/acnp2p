import os
import socket
import hashlib
import sys

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# TODO: Write code to accept cmd line args
#We receive filename. Assume filename is filename

#For generating a hash
BUF_SIZE = 65536
sha1 = hashlib.sha1()

#File to be published
fileName = sys.argv[1]

if os.path.isfile(fileName):
    with open(fileName, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
#print sha1.hexdigest()

    fileHash = sha1.hexdigest()
    #TODO: How to get filetype? Use python-magic or user specified?
    fileType = 'text/html'
    metadata = (fileHash, fileName, fileType)
    endPoint = get_ip_address()
    sequenceNumber = 0 #Initial publisher. How should neighbours publish this?

    #Check if (metadata, endPoint, sequenceNumber) exists in PUBLISHED.csv
