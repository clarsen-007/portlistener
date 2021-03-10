'''    Portlistner
'''
import socket
import sys

PHOST = raw_input('Please enter IP address - generally use 0.0.0.0:      ')
PPORT = input('Please enter PORT number:      ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
print ''
print 'Socket created - on IP: ', PHOST, 'and Port: ', PPORT

try:
    s.bind((PHOST, PPORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete and listening'

s.listen(10)

while 1:

    conn, addr = s.accept()
    print 'Connection from ' + addr[0] + ':' + str(addr[1])
    
s.close()

