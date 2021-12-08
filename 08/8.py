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

INPUT_FILE='8-input.txt'
#INPUT_FILE='8a-example.txt'
#INPUT_FILE='8b-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

digits_segs = {0: {'a', 'b', 'c', 'e', 'f', 'g'},
               1: {'c', 'f'},
               2: {'a', 'c', 'd', 'e', 'g'},
               3: {'a', 'c' ,'d', 'f', 'g'},
               4: {'b', 'c', 'd', 'f'},
               5: {'a', 'b', 'd', 'f', 'g'},
               6: {'a', 'b', 'd', 'e', 'f', 'g'},
               7: {'a', 'c', 'f'},
               8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
               9: {'a', 'b', 'c', 'd', 'f', 'g'}}


# def solver(signals, map):
#     for signal in signals:
#         signal_len = len(signal)
#
#         if signal_len == 2:
#             poss_digits = {1}
#         elif signal_len == 3:
#             poss_digits = {7}
#         elif signal_len == 4:
#             poss_digits = {4}
#         elif signal_len == 5:
#             poss_digits = {2, 3, 5}
#         elif signal_len == 6:
#             poss_digits = {0, 6, 9}
#         elif signal_len == 7:
#             poss_digits = {8}
#
#         found = True
#         for digit in poss_digits:
#             for seg in signal:
#                 if seg in map:
#                     if map[seg] not in digit:
#                         found = False
#                         break
#                 else:
#                     map[seg] = ''
#             pass
#     pass


def solver2(signals):
    def finder_of_len(desired_len):
        return [a for a in signals if len(a) == desired_len]

    map = dict()

    one_digit = finder_of_len(2)[0]

    seven_digit = finder_of_len(3)[0]
    map[(seven_digit - one_digit).pop()] = 'a'

    four_digit = finder_of_len(4)[0]
    four_new_segs = four_digit - one_digit
#    print('4', four_digit, four_new_segs)

    three_digit = None
    for cur in finder_of_len(5):
        temp = cur - (four_digit.union(seven_digit).union(one_digit))
        if len(cur.intersection(one_digit)) == 2:
            map[temp.pop()] = 'g'
            three_digit = cur
            break
#    print('3_digit', three_digit)

#    print(four_digit, three_digit, four_digit - three_digit)
    b_seg = (four_digit - three_digit).pop()
    map[b_seg] = 'b'
#    print(four_new_segs, four_digit, b_seg, (four_new_segs - set(b_seg)).pop())
    map[(four_new_segs - set(b_seg)).pop()] = 'd'

    for cur in finder_of_len(5):
        if len(cur - three_digit) == 0:
            continue
        if b_seg in cur:
            five_digit = cur
            continue
        two_digit = cur

    f_seg = (five_digit - two_digit - set(b_seg)).pop()
    map[f_seg] = 'f'
    c_seg = (one_digit - set(f_seg)).pop()
    map[c_seg] = 'c'

    eight_digit = finder_of_len(7)[0]
    e_seg = (eight_digit - three_digit - set(b_seg)).pop()
    map[e_seg] = 'e'

    return map


counter_1_4_7_8 = 0
sum = 0

for line in input:
    line_split = line.split(' ')
    idx = line_split.index('|')

    signals = sorted([set(x) for x in line_split[0:idx]], key=lambda x: len(x))
    output = [set(x) for x in line_split[idx+1:]]
    mapper = solver2(signals)
    cur_num = ""
    for out in output:
        trans_out = set()
        for cur_seg in out:
            trans_out.add(mapper[cur_seg])

        for cur_digit, cur_digit_segs in digits_segs.items():
            if cur_digit_segs == trans_out:
                cur_num += str(cur_digit)

                if cur_digit in [1, 4, 7, 8]:
                    counter_1_4_7_8 += 1
                break
    sum += int(cur_num)

print('a', counter_1_4_7_8)
print('b', sum)


