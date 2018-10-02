#!/usr/bin/python

initialMsg = "You have now entered the Duck Web, and you're in for a honkin' good time."
xorData = '2906164f2b35301e511b5b144b085d2b50145d00191759525d'.decode('hex')

flag = ''
for i in range(len(xorData)):
	flag += chr(ord(xorData[i]) ^ ord(initialMsg[i]))

print flag
