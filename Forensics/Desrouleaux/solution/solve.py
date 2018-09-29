#!/usr/bin/python

import json

with open('incidents.json') as f:
	data = f.read()

tickets = json.loads(data)['tickets']
for tick in tickets:
	if tick['src_ip'] == '124.80.164.10':
		print tick['dst_ip']

# 162.8.248.12
# 