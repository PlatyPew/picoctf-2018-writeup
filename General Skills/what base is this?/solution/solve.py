#!/usr/bin/python

from pwn import *
import re

s = remote('2018shell1.picoctf.com', 1225)

binary = s.recvuntil('word.')
print binary

binary = re.findall(r'(\d+)', binary)

ans = ''
for i in binary:
	ans += chr(int(i, 2))

print 'SEND> ' + ans
s.sendline(ans)

hexa = s.recvuntil('word').strip()
print hexa

hexa = re.findall(r'([0-9a-f]+) as ', hexa)[0]
ans = hexa.decode('hex')

print 'SEND> ' + ans
s.sendline(ans)

dec = s.recvuntil('word.')[2:]
print dec

dec = re.findall(r'[0-9]+', dec)

print dec
ans = ''
for i in dec:
	ans += chr(int(i, 8))

print 'SEND>' + ans
s.sendline(ans)

print s.recvuntil('}\n')

s.close()