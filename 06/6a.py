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

INPUT_FILE='6-input.txt'
#INPUT_FILE='6a-example.txt'

input = [int(el) for el in get_file_contents(INPUT_FILE)[0][0].split(',')]

def tick(fishes: List[int]) -> List[int]:
    res = []

    new_fish = 0
    for idx, fish in enumerate(fishes):
        if fish == 0:
            new_fish += 1
            res.append(6)
        else:
            res.append(fish-1)

    for i in range(new_fish):
        res.append(8)

    return res

fishes = input.copy()
start_a = time()
for day in range(18):
    fishes = tick(fishes)
    #pprint.pprint(fishes)

print(len(fishes))
print('time a', time() - start_a)

