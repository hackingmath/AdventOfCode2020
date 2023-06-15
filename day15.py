# Advent of Code 2020 Day 8
# https://adventofcode.com/2020/day/8

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

nums = [0,3,1,6,7,5]
numdict = dict()

def find_last(arr,n,testing):
    """Returns difference of indexes of n in arr"""
    if arr.count(n) < 2:
        return False
    output = 0
    idx = len(arr)-1
    while output <= 0:
        if testing:
            print('idx:',idx)
        if arr[idx] == n:
            if testing:
                print("idx,n:",idx,n)
            if output == 0:
                output = -idx
            else:
                return -(output + idx)
        idx -= 1

#print(find_last([0,3,6,0,3,3,1,0,4],0,True))
def part1(arr,turns,testing=False):
    while True:
        n = arr[-1]
        if arr.count(n)== 1:
            arr.append(0)
        else:
            arr.append(find_last(arr,n,testing))
        if len(arr) == turns:
            return arr#[-1]



def part2():
    pass

print("part 1:",part1([0,3,6],30))
#part2()
print("Time (secs):",time.time()-starting_time)