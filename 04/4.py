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

INPUT_FILE='4-input.txt'
#INPUT_FILE='4a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)]

balls = [int(el) for el in input[0][0].split(',')]
board_size = len([el for el in input[1][0].split(' ') if el])

boards = list()
boards_transpose = list()

buf = list()

for line in input[1:]:
    for board_line in line:
        buf.append([int(el) for el in board_line.split(' ') if el])
    boards.append(buf)
    boards_transpose.append(([[buf[j][i] for j in range(board_size)] for i in range(board_size)]))
    buf = list()

## End setting up boards


def looker(balls, boards):
    drawn_balls = set()
    for ball_idx, cur_ball in enumerate(balls):
        drawn_balls.add(cur_ball)
        for board_idx, board in enumerate(boards):
            for line in board:
                if len(drawn_balls.intersection(set(line))) == board_size:
                    return ball_idx, board_idx

        for board_idx, board in enumerate(boards_transpose):
            for line in board:
                if len(drawn_balls.intersection(set(line))) == board_size:
                    return ball_idx, board_idx

start_a = time()
ball_idx, board_idx = looker(balls, boards)
unused = filter(lambda x: x not in balls[:ball_idx+1], chain.from_iterable(boards[board_idx]))
unused_sum = sum(unused)
print('a', unused_sum, balls[ball_idx])
print('a', unused_sum * balls[ball_idx])
print('a time', time()-start_a)

while len(boards) > 1:
    del boards[board_idx]
    del boards_transpose[board_idx]
    ball_idx, board_idx = looker(balls, boards)

unused = filter(lambda x: x not in balls[:ball_idx+1], chain.from_iterable(boards[board_idx]))
unused_sum = sum(unused)
#print('b', ball_idx, board_idx)
#print('b', balls[ball_idx], board_idx + 1)
print('b', unused_sum, balls[ball_idx])
print('b', unused_sum * balls[ball_idx])
print('b time', time()-start_a)
