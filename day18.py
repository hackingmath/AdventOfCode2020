# Advent of Code 2020 Day 18
# https://adventofcode.com/2020/day/18

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day18.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)
    print("eval:",lines[0],eval(lines[0]))
    print("eval test:",eval('6+3+(2*(4+5*3)+2)'))#'5 + (8 * 3 + 9 + 3 * 4 * 3)'))

def part1(testing=False):
    pass


def part2():
    pass

part1()
#part2()
print("Time (secs):",time.time()-starting_time)