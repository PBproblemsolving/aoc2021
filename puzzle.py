list0 = []

with open('aoc2021/input') as f:
    for line in f:
        list0.append(int(line.rstrip('\n')))

list2 = []
x = 0
y = 0

while x < len(list0):
    try: 
        if list0[x] > list0[x-1]:
            list2.append(list0[x])
        if sum(list0[x + 1:x+4]) > sum(list0[x:x + 3]):
            y += 1
    except:
        pass
    x += 1

print(len(list2))
print(y)