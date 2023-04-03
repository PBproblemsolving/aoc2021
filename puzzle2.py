list0 = []
with open('aoc2021/input2') as f:
    for line in f:
        list0.append(line.rstrip('\n'))

list2 = []
for item in list0:
    a = item.split()
    a[1] = int(a[1])
    list2.append(a)

hor, dep, aim = 0, 0, 0

for item in list2:
    if item[0] == 'forward':
        hor += item[1]
        if aim != 0:
            dep += aim * item[1]
    elif item[0] == 'down':
        aim += item[1]
    elif item[0] == 'up':
        aim -= item[1]

print(hor * dep)