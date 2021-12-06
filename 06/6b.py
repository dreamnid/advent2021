#!/usr/bin/env python3
from collections import defaultdict, Counter
from functools import partial, reduce
from itertools import chain, cycle, takewhile, count
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

INPUT_FILE='6-input.txt'
#INPUT_FILE='6a-example.txt'

input = [int(el) for el in get_file_contents(INPUT_FILE)[0][0].split(',')]
input = Counter(input)
#print(input)

def tick(fishes: List[int]) -> List[int]:
    res = defaultdict(int)

    for key, val in fishes.items():
        if key == 0:
            res[8] += val
            res[6] += val
        else:
            res[key-1] += val

    return res

fishes = input.copy()
start_a = time()
for day in range(256):
    fishes = tick(fishes)
    #pprint.pprint(fishes)

print(sum(fishes.values()))
print('time b', time() - start_a)

