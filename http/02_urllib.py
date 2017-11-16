#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import urllib.request
import urllib.parse

params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
url = "http://www.musi-cal.com/cgi-bin/query?%s" % params

with urllib.request.urlopen(url) as f:
	print(f.read().decode('utf-8'))