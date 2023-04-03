list0= set()
folds = []

def fold(folded, folder):
    arg = int(folder[0][2:])
    if folder[0][0] == 'x':
        if folded[0] > arg:
            new_folded = (2*arg-folded[0],folded[1])
            return new_folded
        else:
            return folded
    if folder[0][0] == 'y':
        if folded[1] > arg:
            new_folded = (folded[0],2*arg-folded[1])
            return new_folded
        else:
            return folded

with open('aoc2021/input13') as f:
    for line in f:
        line = line.rstrip('\n')
        try:            
            line = line.split(',')
            for x, item in enumerate(line):
                line[x] = int(line[x])
            list0.add(tuple(line))
        except:
            if line[0]:
                folds.append(line[0].split()[-1:])

print(list0)
print(folds[0])

xMax = 0
yMax = 0



for item in folds:
    newlist = set()
    for dot in list0:
        after_fold = fold(dot, item)
        newlist.add(after_fold)
    list0 = newlist.copy()

for item in list0:
    if item[0] > xMax:
        xMax = item[0]
    if item[1] > yMax:
        yMax = item[1]

for i in range(yMax+1):
    print('\n')
    for j in range(xMax+1):
        if (j, i) in list0:
            print('#',end='')
        else:
            print('.',end='')
print(len(list0))