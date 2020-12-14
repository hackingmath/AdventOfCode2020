#day 2
with open("day2.txt") as f:
    lst = []
    for line in f.readlines():
        lst.append([x for x in line.split()])

    
print(lst[:10])

def unpack(arr):
    nums = arr[0].split("-")
    min_num,max_num = int(nums[0]),int(nums[-1])
    letter = arr[1][0]
    pwd = arr[2]
    freq = pwd.count(letter)
    return min_num <= freq <= max_num

print(sum([1 for x in lst if unpack(x)]))
# 564, Correct!

#day 2 part 2

def unpack2(arr):
    nums = arr[0].split("-")
    first,last = int(nums[0]),int(nums[-1])
    letter = arr[1][0]
    pwd = arr[2]
    if pwd[first-1] == letter and pwd[last-1] == letter:
        return False
    if pwd[first-1] == letter or pwd[last-1] == letter:
        return True

print(sum([1 for x in lst if unpack2(x)]))
#correct: 325
