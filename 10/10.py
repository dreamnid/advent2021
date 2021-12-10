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

INPUT_FILE='10-input.txt'
#INPUT_FILE='10a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

end_char_mapper = {
    '{': '}',
    '[': ']',
    '<': '>',
    '(': ')',
}

corrupt_score_mapper = {
    '}': 1197,
    '>': 25137,
    ')': 3,
    ']': 57,
}

incomplete_score_mapper = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def calculate_scores():
    corrupt_score = 0
    incomplete_scores = []

    for line in input:
        stack = []
        valid = True
        for char in line:
            #print(char, end='')
            if char in end_char_mapper.keys():
                stack.append(char)
            else:
                end_char = end_char_mapper[stack.pop()]
                if char == end_char:
                    continue
                valid = False
                break
        #print()

        #print(line, valid, end_char)
        if not valid:
            corrupt_score += corrupt_score_mapper[char]
            continue

        incomplete_score = 0
        for char in stack[-1::-1]:
            incomplete_score *= 5

            incomplete_score += incomplete_score_mapper[end_char_mapper[char]]
        incomplete_scores.append(incomplete_score)

    incomplete_scores = sorted(incomplete_scores)

    return corrupt_score, incomplete_scores


scores = calculate_scores()
print('a', scores[0])
print('b', scores[1][math.floor(len(scores[1])/2)-1])

