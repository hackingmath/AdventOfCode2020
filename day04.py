#Day 4
with open("day4.txt") as f:
    lst = []
    for line in f.readlines():
        lst.append([x for x in line.split()])
    newlst = []
    item = []
    for i in range(len(lst)-1):
        
        if lst[i] == []:
            newlst.append(item)
            item = []
        else:
            item += lst[i]
    lst = newlst[::]
        
print(lst[:5])

valid_passports = 0
 
for p in lst:
    valids = set()
    for i in p:
        if 'iyr' in i: valids.add('iyr')
        if 'byr' in i: valids.add('byr')
        if 'eyr' in i: valids.add('eyr')
        if 'hgt' in i: valids.add('hgt')
        if 'hcl' in i: valids.add('hcl')
        if 'ecl' in i: valids.add('ecl')
        if 'pid' in i: valids.add('pid')

    if len(valids) > 6:
        valid_passports += 1
    
print(valid_passports) # 190 Correct!

#Day 4 Part 2
with open("day4.txt") as f:
    lst = []
    for line in f.readlines():
        lst.append([x for x in line.split()])
    newlst = []
    item = []
    for i in range(len(lst)-1):
        
        if lst[i] == []:
            newlst.append(item)
            item = []
        else:
            item += lst[i]
    lst = newlst[::]
        
print(lst[:5])

valid_passports = 0
 
for p in lst:
    valids = set()
    for i in p:
        if 'iyr' in i: 
            idx = i.index(':')
            num = i[(idx+1):]
            #print(num)
            if 2010 <= int(num) <= 2020:
                #print("valid")
                valids.add('iyr')
        if 'byr' in i: 
            #print(i)
            idx = i.index(':')
            num = i[(idx+1):]
            #print(num)
            if 1920 <= int(num) <= 2002:
                #print("valid")
                valids.add('byr')

        if 'eyr' in i: 
            idx = i.index(':')
            num = i[(idx+1):]
            #print(num)
            if 2020 <= int(num) <= 2030:
                #print("valid")
                valids.add('eyr')
        if 'hgt' in i: valids.add('hgt')
        if 'hcl' in i: valids.add('hcl')
        if 'ecl' in i: valids.add('ecl')
        if 'pid' in i: valids.add('pid')

    if len(valids) > 6:
        valid_passports += 1
    
print(valid_passports)
