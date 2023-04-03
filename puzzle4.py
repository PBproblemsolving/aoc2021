def addColumn(grid, x):
    sum = 0
    try:
        for item in grid:
            sum += int(item[x])
        return sum
    except:
        return False

def addRow(grid, y):
    sum = 0
    try:
        for item in grid[y]:
            sum += int(item)
    except:
        return False

class GetOutOfLoop( Exception ):
    pass

list0 = []
numbers_drawn = []
midlist = []

with open('aoc2021/input4') as f:
    for x, line in enumerate(f):
        if x == 0:
            numbers_drawn = line.rstrip('\n').split(',')
        else:
            if line == '\n':
                if midlist != []:
                    list0.append(midlist)
                    midlist = []
            else:
                midline = line.rstrip('\n').split()
                midlist.append(midline)

emptylist = []
midlist = []

for x in range(len(list0)+1):
    if midlist != []:
        emptylist.append(midlist)
    midlist = []
    midline = []
    for y in range(6):
        if midline != []:
            midlist.append(midline)
        midline = []
        for z in range(5):
            midline.append('X')

firstgrid = []
lastnumber = 0
try:
    for number in numbers_drawn:
        for x, item in enumerate(list0):
            for y, line in enumerate(item):
                for z, pos in enumerate(line):
                    if pos == number:
                        emptylist[x][y][z] = number
                        if addColumn(emptylist[x], z) or addRow(emptylist[x], y):
                            firstgrid = emptylist[x]
                            lastnumber = int(pos)
                            raise GetOutOfLoop
except GetOutOfLoop:
    sum = 0
    for y, line in enumerate(list0[x]):
        for z, pos in enumerate(line):
            if pos != firstgrid[y][z]:
                sum += int(pos)
    print(sum* lastnumber)


emptylist = []
midlist = []

for x in range(len(list0)+1):
    if midlist != []:
        emptylist.append(midlist)
    midlist = []
    midline = []
    for y in range(6):
        if midline != []:
            midlist.append(midline)
        midline = []
        for z in range(5):
            midline.append('X')

firstgrid = []
lastnumber = 0
adblist = list0[:]
bfsort = []

try:
    for number in numbers_drawn:
        for x, item in enumerate(list0):
            for y, line in enumerate(item):
                for z, pos in enumerate(line):
                    if pos == number:
                        emptylist[x][y][z] = number
                        if addColumn(emptylist[x], z) or addRow(emptylist[x], y):
                            firstgrid = emptylist[x]
                            lastnumber = int(pos)
                            bfsort = item
                            try:
                                adblist.remove(item)
                            except:
                                pass
                            if len(adblist) == 1:
                                raise GetOutOfLoop
except GetOutOfLoop:
    sum = 0
    print(firstgrid)
    print(bfsort)
    for y, line in enumerate(bfsort):
        for z, pos in enumerate(line):
            if pos != firstgrid[y][z]:
                sum += int(pos)
    print(sum* lastnumber)
