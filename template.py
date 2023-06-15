# Advent of Code 2020 Day 8
# https://adventofcode.com/2020/day/8

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day08.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)

def part1(testing=False):
    pass


def part2():
    pass

part1()
#part2()
print("Time (secs):",time.time()-starting_time)