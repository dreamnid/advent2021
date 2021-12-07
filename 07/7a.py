#!/usr/bin/env python3
from collections import defaultdict, Counter
from functools import partial, reduce
from itertools import chain, cycle, takewhile
import math
from operator import mul
import os
import pprint
import re
from statistics import mode
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

INPUT_FILE='7-input.txt'
#INPUT_FILE='7a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]
input = sorted([int(el) for el in input[0].split(',')])

def calc_fuel(pos, crabs):
    return sum(map(lambda x: abs(x-pos), crabs))

pivot = mode(input)

cur = calc_fuel(pivot, input)
while True:
    attempt = calc_fuel(pivot+1, input)
    if attempt > cur:
        break
    pivot += 1
    cur = attempt

while True:
    attempt = calc_fuel(pivot-1, input)
    if attempt > cur:
        break
    pivot -= 1
    cur = attempt

print(pivot, cur)
