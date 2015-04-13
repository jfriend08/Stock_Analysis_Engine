#!/usr/bin/env python
from operator import itemgetter
import sys, re

cur_industry = None
for line in sys.stdin:    
    line = line.strip() # remove leading and trailing whitespace
    fields = line.split("\t")

    M = re.search("[A-Za-z]", fields[1])
    print