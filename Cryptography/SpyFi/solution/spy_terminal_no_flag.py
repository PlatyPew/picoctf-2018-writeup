#!/usr/bin/python2 -u
from Crypto.Cipher import AES

KEY = '6b686164736875617364686e7575666a'

agent_code = """flag"""

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    return cipher.encrypt(plain).encode('hex')

welcome = "Welcome, Agent 006!"
print welcome

sitrep = raw_input("Please enter your situation report: ")
message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
""".format( sitrep, agent_code )
print '-' * 40 + '\n' + message + '\n' + '-' * 40
message = pad(message)
print '-' * 40 + '\n' + message + '\n' + '-' * 40

enc = encrypt(KEY, message )
print '3rd block: ' + enc[3*32:][:32]
print 'Last block: ' + enc[-32:]
