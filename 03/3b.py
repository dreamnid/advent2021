#!/usr/bin/env python3
from collections import defaultdict, Counter
from functools import partial, reduce
from itertools import chain, cycle, takewhile
import math
from operator import mul
import os
import pprint
import re
from time import time
from typing import Dict, List, Set, Tuple, Union

from humanize import intcomma

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='3-input.txt'
#INPUT_FILE='3a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

line_len = len(input[0])
file_len = len(input)
oxy_list = input.copy()
co2_list = input.copy()

for col_idx in range(line_len):
    if len(oxy_list) > 1:
        c_oxy = Counter([line[col_idx] for line in oxy_list])
        if c_oxy['0'] <= c_oxy['1']:
            oxy_filter_val = '1'
        else:
            oxy_filter_val = '0'

        oxy_list = list(filter(lambda x: x[col_idx] == oxy_filter_val, oxy_list))

    if len(co2_list) > 1:
        c_co2 = Counter([line[col_idx] for line in co2_list])
        if c_co2['0'] <= c_co2['1']:
            co2_filter_val = '0'
        else:
            co2_filter_val = '1'

        co2_list = list(filter(lambda x: x[col_idx] == co2_filter_val, co2_list))
    #print(oxy_list, co2_list)

    if len(oxy_list) == 1 and len(co2_list) == 1:
        break

oxy = ''.join(oxy_list)
co2 = ''.join(co2_list)
print(oxy, co2)

oxy_int = int(oxy, 2)
co2_int = int(co2, 2)

print(oxy_int, co2_int)
print(oxy_int * co2_int)
