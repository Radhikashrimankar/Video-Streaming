import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new

HOST=' '
PORT=7000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('Socket created')

s.bind((HOST,PORT))
print ('Socket bind complete')
s.listen(10)
print ('Socket now listening')

conn,addr=s.accept()

### new
data = b""
payload_size = struct.calcsize("L") #Return the size of the struct (and hence of the string) corresponding to the given format
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0] #Unpack the string (presumably packed by pack(fmt, ...)) according to the given format. 
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    ###

    frame=pickle.loads(frame_data)#Read a pickled object representation from the open file object file and return the reconstituted object hierarchy specified therein
    print (frame)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1) & 0xFF

    if key==27:
        cv2.destroyAllWindows()
        break
