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

INPUT_FILE='9-input.txt'
#INPUT_FILE='9a-example.txt'

input = [[int(col) for col in line] for line in get_file_contents(INPUT_FILE)[0]]

num_rows = len(input)
num_cols = len(input[0])

def find_low_points():
    low_points = list()
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            is_min = True
            if i > 0:
                is_min &= col < input[i-1][j]

            if i < num_rows - 1:
                is_min &= col < input[i+1][j]

            if j > 0:
                is_min &= col < input[i][j-1]

            if j < num_cols - 1:
                is_min &= col < input[i][j+1]

            if is_min:
                low_points.append((i, j))

    return low_points

def find_basin_size(row, col, seen=None):
    if seen is None:
        seen = set()
    size = 0
    cur_el = input[row][col]
    seen.add((row, col,))
    #print(row, col, input[row][col], False)
    if row > 0 and input[row-1][col] != 9 and input[row-1][col] > cur_el and (row-1, col,) not in seen:
        #print(row-1, col, input[row-1][col], True)
        size += 1 + find_basin_size(row - 1, col, seen)

    if row < num_rows - 1 and input[row+1][col] != 9 and input[row+1][col] > cur_el and (row+1, col,) not in seen:
        #print(row+1, col, input[row+1][col], True)
        size += 1 + find_basin_size(row + 1, col, seen)

    if col > 0 and input[row][col-1] != 9 and input[row][col-1] > cur_el and (row, col-1,) not in seen:
        #print(row, col-1, input[row][col-1], True)
        size += 1 + find_basin_size(row, col - 1, seen)

    if col < num_cols - 1 and input[row][col+1] != 9 and input[row][col+1] > cur_el and (row, col+1,) not in seen:
        #print(row, col+1, input[row][col+1], True)
        size += 1 + find_basin_size(row, col + 1, seen)

    return size


print('a', sum([1+input[row][col] for row, col in find_low_points()]))

basin_sizes = list()
for row, col in find_low_points():
    basin_sizes.append(find_basin_size(row, col)+1)
    #print(basin_sizes[-1])
    #print('--------------')

print('b', math.prod(sorted(basin_sizes)[-3:]))
