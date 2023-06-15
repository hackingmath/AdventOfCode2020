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
    acc = 0
    idx = 0
    visited = set()
    while True:
        if testing:
            print("idx:",idx)
        #for line in lines:
        if idx in visited:
            return acc
        else:
            visited.add(idx)
        line = lines[idx].split(' ')
        if line[0] == 'jmp':
            amt = int(line[1][1:])
            if testing:
                print("amt:",amt)
            if line[1][0] == '+':
                idx += amt
            else:
                idx -= amt
        elif line[0] == 'acc':
            accamt = int(line[1][1:])
            if testing:
                print("accamt:",accamt)
            if line[1][0] == '+':
                acc += accamt
            else:
                acc -= accamt
            idx += 1
        else: #'nop'
            idx += 1


def do_loop(arr,testing):
    acc = 0
    idx = 0
    visited = set()
    while True:
        if testing:
            print("idx:",idx)
        #for line in lines:
        if idx in visited:
            return "Loop"
        else:
            visited.add(idx)
        if idx >= len(arr):
            return acc
        line = arr[idx].split(' ')
        if line[0] == 'jmp':
            amt = int(line[1][1:])
            if testing:
                print("amt:",amt)
            if line[1][0] == '+':
                idx += amt
            else:
                idx -= amt
        elif line[0] == 'acc':
            accamt = int(line[1][1:])
            if testing:
                print("accamt:",accamt)
            if line[1][0] == '+':
                acc += accamt
            else:
                acc -= accamt
            idx += 1
        else: #'nop'
            idx += 1

def part2(testing=False):
    newlines = lines[::]
    for i,line in enumerate(newlines):
        line = line.split(' ')
        if testing:
            print("line:",line)
        if line[0] == 'jmp':
            if testing:
                print("jmp found")
            newlines[i] = newlines[i].replace('jmp','nop')
            attempt = do_loop(newlines,False)
            if attempt == "Loop":
                newlines[i] = newlines[i].replace('nop', 'jmp')
                continue
            else:
                print("Part 2",attempt)
                return
        if testing:
            print("new lines:",newlines)



#print("Part 1:",part1())
part2()
#print(do_loop(True))
print("Time (secs):",time.time()-starting_time)