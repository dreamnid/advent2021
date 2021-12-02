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

INPUT_FILE='1-input.txt'
#INPUT_FILE='1a-example.txt'

input = [int(line) for line in get_file_contents(INPUT_FILE)[0]]

old = input[0]
increased_count = 0

for idx, level in enumerate(input):
    if idx == 0:
        continue

    if level > old:
        increased_count += 1
    #print(level, old, increased_count)
    old = level

print(increased_count)