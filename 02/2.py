#!/usr/bin/env python3
from collections import defaultdict
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

INPUT_FILE='2-input.txt'
INPUT_FILE='2a-example.txt'

x = 0
y = 0

input = [line for line in get_file_contents(INPUT_FILE)[0]]

for line in input:
    parts = line.split(' ')
    val = int(parts[1])
    if parts[0] == 'forward':
        x += val
    elif parts[0] == 'down':
        y += val
    elif parts[0] == 'up':
        y -= val

print('x', x, 'y', y, 'x*y', x*y)

