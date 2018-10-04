#!/usr/bin/python
from gmpy2 import *

c = 7929011382767041584510203527859505899601572024468762886720475415218105799874362
n = 11930191517420424428458862771846268087893161863249464023139623203854660066472157
e = 65537

p = 92027970011808537690210426025129587299
q = 129636582398694722475936463924386691191743

def eea(a,b):
	if b==0:return (1,0)
	(q,r) = (a//b,a%b)
	(s,t) = eea(b,r)
	return (t, s-(q*t) )

def find_inverse(x,y):
	inv = eea(x,y)[0]
	if inv < 1: inv += y #we only want positive values
	return inv

totient = (p - 1) * (q - 1)

d = find_inverse(e, totient)
flag = powmod(c, d, n)

print hex(flag)[2:].decode('hex')
