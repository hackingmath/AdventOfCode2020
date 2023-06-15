# Advent of Code 2020 Day 8
# https://adventofcode.com/2020/day/8

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day09.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [int(x.strip("\n")) for x in lines]
    print(len(lines),lines)

def is_sum(arr,n):
    """Returns True if there are 2 numbers in
    arr that sum to n"""
    for x in arr:
        if n-x in arr:
            return True
    return False

#print(is_sum(40,[35,20,15,25,47]))
def part1(arr,length,testing=False):
    idx = 0
    while True:
        num = arr[idx+length+1]
        numrange = arr[idx:idx+length+1]
        if is_sum(numrange,num):
            idx += 1
            continue
        print(num,numrange)
        print([num-x for x in numrange])
        return

def part2(arr=lines,num=375054920,testing=False):
    idx = 0
    length = 2
    while True:
        numrange = arr[idx:idx + length]
        if testing:
            print("numrange:",numrange)
        if sum(numrange)==num:
            print("part 2:",min(numrange) + max(numrange))
            return
        elif sum(numrange) > num:
            idx += 1
            length = 2
        else:
            length += 1
        #print(num, numrange)
        #print([num - x for x in numrange])
    return False

#part1(lines,25) #6571 too low. Correct: 375054920
part2(lines,375054920,False)
print("Time (secs):",time.time()-starting_time)