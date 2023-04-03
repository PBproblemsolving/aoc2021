def dome(y, x, cave):
    smaller = 0
    try:
        if cave[y][x] >= cave[y+1][x]:
            smaller += 1
    except:
        pass
    if y > 0:
        if cave[y][x] > cave[y-1][x]:
            smaller += 1

    if x > 0:
        if cave[y][x] > cave[y][x-1]:
            smaller += 1

    try:
        if cave[y][x] >= cave[y][x+1]:
            smaller += 1
    except:
        pass
    return smaller

def localdome(y, x, cave):
    toreturn = []
    try:
        if cave[y][x] < cave[y+1][x]:
            if cave[y+1][x] != 9:
                toreturn.append((y+1,x))
    except:
        pass
    if y > 0:
        if cave[y][x] < cave[y-1][x]:
            if cave[y-1][x] != 9:
                toreturn.append((y-1,x))

    if x > 0:
        if cave[y][x] < cave[y][x-1]:
            if cave[y][x-1] != 9:
                toreturn.append((y,x-1))

    try:
        if cave[y][x] < cave[y][x+1]:
            if cave[y][x+1] != 9:
                toreturn.append((y,x+1))
    except:
        pass
    return toreturn

def basin(y, x, cave):
    lnumbers = []
    lnumbers.append((y,x))
    for item in lnumbers:
        lnumbers += localdome(item[0],item[1], cave)
    return lnumbers


list0 = []
with open('aoc2021/input9') as f:
    for line in f:
        line = (list(line.rstrip('\n')))
        for x, item in enumerate(line):
            line[x] = int(item)
        list0.append(line)

risk = 0

for x, item in enumerate(list0):
    for y, item2 in enumerate(item):
        if not dome(x, y, list0):
            risk += item2 + 1

print(risk)
listofkurwa = []

for x, item in enumerate(list0):
    for y, item2 in enumerate(item):
        if not dome(x, y, list0):
            dsdsd = basin(x, y, list0)
            listofkurwa.append(len(set(dsdsd)))

listofkurwa.sort()

sum = listofkurwa[-1]*listofkurwa[-2]*listofkurwa[-3]

print(sum)