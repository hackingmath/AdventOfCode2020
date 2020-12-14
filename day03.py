with open("day3.txt") as f:
    field = []
    for line in f.readlines():
        field.append([200*x for x in line.split()])

# print(field[:10])
# print(len(field[0][0]))
print("rows:",len(field))

def slopes(right,down):
    trees = 0
    row, col = 0,0
    while row < len(field):
        if field[row][0][col] == '#':
            trees += 1
        col += right
        row += down
        #print("row,col:",row,col)
    return trees

arr = [(1,1),(3,1),(5,1),(7,1),(1,2)]
ans = [slopes(c,r) for (c,r) in arr]
output = 1
for a in ans:
    output *= a
print("output:",output)
print('ans:',ans)
    
    
print(slopes(3,1))
