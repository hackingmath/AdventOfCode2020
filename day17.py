# Advent of Code 2020 Day 17 Conway Cubes
# https://adventofcode.com/2020/day/17

import time
#from random import randint
from itertools import combinations

starting_time = time.time()
GRID_H = 3
GRID_W = 3
GRID_Z = 3
class Cell(object):
    def __init__(self,x,y,z,state):
        self.x = x
        self.y = y
        self.z = z
        self.state = state

    def checkNeighbors(self):
        # if self.state == 1: return 1 #on cells stay on
        neighbs = 0  # check the neighbors
        for dx,dy,dz in [[-1, 0, 0], [-1, 0, 1], [-1, 0, -1],
                       [-1, -1, 0], [-1, -1, 1], [-1, -1, -1],
                       [-1, 1, 0], [-1, 1, 1], [-1, 1, -1],
                       [1, 0, 0], [1, 0, 1], [1, 0, -1],
                       [1, -1, 0], [1, -1, 1], [1, -1, -1],
                       [1, 1, 0], [1, 1, 1], [1, 1, -1],
                       [0, 0, 1], [0, 0, -1],
                       [0, -1, 0], [0, -1, 1], [0, -1, -1],
                       [0, 1, 0], [0, 1, 1], [0, 1, -1],
                       ]:
            try:
                if cellList[self.x + dx][self.y + dy][self.z + dz].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if self.state == 1:
            if neighbs in [2, 3]:
                return 1
            return 0
        if neighbs == 3:
            return 1
        return 0

with open('day17.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)

def createCellList(arr):
    '''Creates a big list of cells'''
    newList = [] #empty list for cells
    #populate the initial cell list
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
            newList[j].append([])
            for k in range(GRID_Z):
                newList[j][i].append([])
    for r,row in enumerate(arr):
        for c,col in enumerate(row):
            if col == '#':
                newList[r][c][GRID_Z//2].append(Cell(r,c,GRID_Z//2,1))
            else:
                newList[r][c][GRID_Z // 2].append(Cell(r, c, GRID_Z // 2, 0))

    return newList

def display_cells(arr,zcor):
    for r,row in enumerate(arr):
        for c,col in enumerate(row):
            if arr[r][c][zcor].state == 1:
                print('#')
            else:
                print('.')
        print()
def encode(a,b,c):
    """My idea to store the xyz coords of a
    cube with strings so it can be the key of
    a dictionary:
    encode(1,3,4) -> '001003004'
    cubes['001003004'] = 'ON'"""
    strabc = [str(a),str(b),str(c)]
    output = ''
    for x in strabc:
        diff = 3 - len(x)
        if diff > 0:
            x = '0'*diff + x
            output += x
    return output #str(a)+str(b)+str(c)

#print(encode(1,3,4))

def decode(numstr):
    """Decode string back to list of numbers"""
    a,b,c = int(numstr[:3]),int(numstr[3:6]),int(numstr[6:])
    return tuple([a,b,c])

#print(decode('012033027'))
def part1(testing=False):
    testarr = ['.#.','..#','###']
    cellarr = createCellList(testarr)
    print(cellarr)
    display_cells(cellarr,0)


def part2():
    pass

part1()
#part2()
print("Time (secs):",time.time()-starting_time)