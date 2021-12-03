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

res_list = list()
for col_idx in range(line_len):
    c = Counter([line[col_idx] for line in input])
    if c['0'] > c['1']:
        res_list.append('0')
    else:
        res_list.append('1')



gamma = ''.join(res_list)
epsilon = gamma.translate({**gamma.maketrans('1', '0'), **gamma.maketrans('0', '1')})
print(gamma, epsilon)
gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print(gamma_int, epsilon_int)
print(gamma_int * epsilon_int)
