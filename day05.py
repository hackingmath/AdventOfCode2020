#Day 5 Part 1

from math import ceil

def average(a,b):
    return (a+b)/2

def seat(str):
    lower,upper=0,127
    for letter in str[:-3]:
        if letter == 'F':
            upper = int(average(lower,upper))
        else:
            lower = ceil(average(lower,upper))
        #print(lower,upper)
    row = average(lower,upper)
    lower,upper = 0,8
    for letter in str[-3:]:
        if letter == 'L':
            upper = int(average(lower,upper))
        else:
            lower = ceil(average(lower,upper))
        #print(lower,upper)
    col = int(average(lower,upper))
    return row*8 + col

with open("day5.txt") as f:
    lst = []
    for line in f.readlines():
        for x in line.split():
            lst.append(x)
            
seats = [int(seat(i)) for i in lst]
print(seats[:10])

for i in range(1,832):
    if i not in seats:
        print(i)
        
print(max(seats)) #832
