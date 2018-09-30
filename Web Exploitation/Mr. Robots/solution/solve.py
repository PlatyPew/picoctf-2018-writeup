#!/usr/bin/python

import requests
import re

r = requests.get('http://2018shell1.picoctf.com:10157/robots.txt')
source = r.text
page = re.findall(r'Disallow: /(.+)', source)[0]
print 'Found: ' + page

r = requests.get('http://2018shell1.picoctf.com:10157/{}'.format(page))
source = r.text
print re.findall(r'(picoCTF\{.+\})', source)[0]
