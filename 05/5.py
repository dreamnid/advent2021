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

INPUT_FILE='5-input.txt'
#INPUT_FILE='5a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

def solver(include_diags=False):
    board = defaultdict(lambda: defaultdict(int))

    for line in input:
        line_split = line.split(' -> ')
        first_coords = tuple(map(int, line_split[0].split(',')))
        second_coords = tuple(map(int, line_split[1].split(',')))

        if first_coords[0] == second_coords[0]:
            tmp = (first_coords[1], second_coords[1],)
            for x in range(min(tmp), max(tmp)+1):
                board[x][first_coords[0]] += 1
        elif first_coords[1] == second_coords[1]:
            tmp = (first_coords[0], second_coords[0],)
            for y in range(min(tmp), max(tmp)+1):
                board[first_coords[1]][y] += 1
        elif include_diags:
            if first_coords[0] < second_coords[0]:
                start_coord = first_coords
                end_coord = second_coords
            else:
                start_coord = second_coords
                end_coord = first_coords

            if start_coord[1] < end_coord[1]:
                multiplier = 1
            else:
                multiplier = -1

            for i in range(end_coord[0]-start_coord[0]+1):
                board[start_coord[1]+i*multiplier][start_coord[0] + i] += 1

    return board

start_a = time()
lines_cross = 0
for row in solver().values():
    lines_cross += len(tuple(filter(lambda x: x > 1, row.values())))

print(lines_cross)
print('time a', time() - start_a)
print()

start_b = time()
lines_cross = 0
for row in solver(include_diags=True).values():
    lines_cross += len(tuple(filter(lambda x: x > 1, row.values())))

print(lines_cross)
print('time b', time() - start_b)
