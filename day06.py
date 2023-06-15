# Day 6

from collections import Counter

with open("day06.txt") as f:
    #text_strings = f.read()
    lst = [line.split('\n') for line in f.readlines()]
#     for line in f.readlines():
#         for x in line.split('\n'):
#             lst.append(x)
    print(len(lst),lst[-3:])

letters = set()
groups = list()
group = list()
for x in lst:
    if x[0] != '':
        group.append(x[0])
    else:
        groups.append(group)
        group = list()
groups.append(['fcelpwgamhnquzbsrtdxivjk','tdjwzsaqhxunkfcvpbrmgil'])
print(groups)

def in_all(stringlist,letter):
    """Returns True if letter is in
    every string in stringlist"""
    for s in stringlist[1:]:
        if letter not in s:
            return False
    return True

testlist = ['rahgpijvyfd', 'biwvrajyp', 'ajbrvopeiyw']
# for s in testlist[0]:
#     print(s,"in_all?",in_all(testlist,s))

testlist2 = [['a'],['abc','b']]
def part2(testing=False):
    counts = 0
    for i,l in enumerate(groups): #list of strings
        firstword = l[0]
        for letter in firstword:
            if in_all(l,letter):
                if testing:
                    print("group:",i,"letter:",letter)
                counts += 1
    print("Matches:",counts)

part2() #3562 too low


def part2OLD(arr):
    running_sum = 0
    while True:
        letters = []
        group = []
        for i, v in enumerate(arr):
            if v[0]:
                group.append(v[0])
                for letter in v[0]:
                    if letter not in letters:
                        letters.append(letter)
                        #print("letters:", letters)
            else:
                for letter in letters:
                    for g in group:
                        if sum([1 for i in group]):
                            pass #???


sample = [['qpicundo', ''], ['fiqcdbkyuoz', ''], ['', ''],
          ['rahgpijvyfd', ''], ['biwvrajyp', ''], ['ajbrvopeiyw', ''], ['', ''],
          ['cv', ''], ['v', ''], ['qwvo', ''], ['v', '']]

#print(part2(sample))


def parse(string):
    out = []
    groups = string.split('\n\n')  # Split by empty line
    for group in groups:
        strings = [item.strip() for item in group.split('\n')]
        new_group = ''  # set()
        for thing in strings:
            new_group += thing
        out.append(new_group)
    return out


#parsed = parse(text_strings)
#print("parsed:",parsed)

def count_yes(string):
    questions = set()
    for s in string:
        questions.add(s)
    return len(questions)

#print("Part 1:",sum([count_yes(i) for i in parsed])) #6930

#From Joel Grus:
def count_yeses2():
    #groups = raw.split("\n\n")
    num_yeses = 0
    for people in groups:
        #people = group.split("\n")
        yeses = Counter(c for person in people for c in person)
        num_yeses += sum(count == len(people) for c, count in yeses.items())
    return num_yeses

print("Joel's soln:",count_yeses2()) #also 3562 but his answer for Part 1 was low

#Fogleman: #also 3562
for f in [set.union, set.intersection]:
    print("Fogleman's soln:",sum(len(f(*map(set, g))) for g in groups))