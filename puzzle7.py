def math(a):
    sum = 0
    i = 1
    while a >= i:
        sum += i
        i += 1
    return sum

def fuel(goal, present, mul):
    diff = abs(goal-present)
    return math(diff)*mul


list0 = []
with open('aoc2021/input7') as f:
    for line in f:
        list0 = line.rstrip('\n').split(',')

for x, item in enumerate(list0):
    list0[x] = int(item)

dictofcrabs = dict()

for item in list0:
    try:
        dictofcrabs[item] += 1
    except:
        dictofcrabs[item] = 1

cheapest = 11111111111111111

list2 = []

for x in dictofcrabs:
    list2.append(x)

list2.sort()

for i in range(list2[-1]+1):
    

    local = 0
    for a, b in dictofcrabs.items():
        local += fuel(i, a, b)
    if cheapest > local:
        cheapest = local

print(cheapest)