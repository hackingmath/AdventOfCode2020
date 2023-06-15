# Advent of Code 2020 Day 20
# https://adventofcode.com/2020/day/20

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day20.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)
    tiles = [x for x in lines if x != '']
    print(len(tiles),tiles[:5])
    print("Tiles:",sum([1 for x in tiles if x[0]=='T'])) #144 so 12x12

def part1(testing=False):
    pass


def part2():
    pass

part1()
#part2()
print("Time (secs):",time.time()-starting_time)