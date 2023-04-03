import copy

def determine(fish):
    if fish == 0:
        return False
    else:
        return True

list0 = []

with open('aoc2021/input6') as f:
    for line in f:
        list0 = line.rstrip('\n').split(',')


for x, item in enumerate(list0):
    list0[x] = int(item)

dictoffish = dict(zip(reversed(range(9)), [0] * 9))

for item in list0:
    dictoffish[item] += 1


print(dictoffish)
for i in range(256):
    newdict = dict(zip(reversed(range(9)), [0] * 9))
    newdict[8] = dictoffish[0]
    newdict[6] = dictoffish[0] + dictoffish[7]
    for key in dictoffish:
        if key == 0:
            newdict[8] = dictoffish[0]
            newdict[6] = dictoffish[0] + newdict[6]
        else:
            newdict[key-1] = dictoffish[key]

    dictoffish = dict((k, v) for k,v in newdict.items())

value = 0 
for key in dictoffish:
    value += dictoffish[key]

print(value)