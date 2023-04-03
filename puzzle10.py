class FoundCorrupted (Exception):
    pass

list0 = []
with open('input10') as f:
    for line in f:
        list0.append(line.rstrip('\n'))


openings = ['(', '[', '{', '<']
closures = [')', ']', '}', '>']
listofpairs = []

scoredict = {')': 3, ']': 57, '}': 1197, '>': 25137}
score = 0
uncomplited = []

for line in list0:
    pairings = []
    try:
        for char in line:
            if char in openings:
                pairings.append([char,''])
            else:
                for x, item in reversed(list(enumerate(pairings))):
                    if not item[1]:
                        pairings[x][1] = char
                        if openings.index(pairings[x][0]) != closures.index(pairings[x][1]):
                            score += scoredict[char]
                            raise FoundCorrupted
                        break               
    except FoundCorrupted:
        continue
    uncomplited.append(line)    

print(score)

lcompscores = []

dcompscores = {')': 1, ']': 2, '}': 3, '>': 4}


for line in uncomplited:
    compscore = 0
    pairings = []
    lacking = ''
    for char in line:
        if char in openings:
            pairings.append([char,''])
        else:
            for x, item in reversed(list(enumerate(pairings))):
                if not item[1]:
                    pairings[x][1] = char
                    break
    for item in pairings:
        if not item[1]:
            lacking += closures[openings.index(item[0])]
    for item in reversed(lacking):
        compscore = compscore * 5 + dcompscores[item]
    lcompscores.append(compscore)

lcompscores.sort()

print(lcompscores[len(lcompscores)//2])