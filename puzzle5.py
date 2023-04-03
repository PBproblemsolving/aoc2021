list0 = []

with open('aoc2021/input5') as f:
    for line in f:
        line = line.rstrip('\n').split(' -> ')
        midlist = []
        for item in line:
            item = item.split(',')
            item[0] = int(item[0])
            item[1] = int(item[1])
            midlist.append(item)

        list0.append(midlist)
        
# bigX = 0
# bigY = 0        

# for item in list0:
#     if item[1][0] > bigX:
#         bigX = item[1][0]
#     if item[1][1] > bigY:
#         bigY = item[1][1]

bigX = 1000
bigY = 1000 

gameGrid = []

for x in range(bigX):
    midlist = []
    for y in range(bigY):
        midlist.append(0)
    gameGrid.append(midlist)


for item in list0:
    if item[0][0] == item[1][0]:
        for x in range(abs(item[1][1] - item[0][1])+1):
            if item[1][1] - item[0][1] < 0:
                x = -x
            gameGrid[item[0][1]+x][item[0][0]] += 1
    elif item[0][1] == item[1][1]:
        for x in range(abs(item[1][0] - item[0][0])+1):
            if item[1][0] - item[0][0] < 0:
                x = -x
            gameGrid[item[0][1]][item[0][0]+x] += 1
    else:
        for x in range(abs(item[1][1] - item[0][1])+1):
            y = x
            if item[1][1] - item[0][1] < 0:
                y = -y
            if item[1][0] - item[0][0] < 0:
                x = -x
            gameGrid[item[0][1]+y][item[0][0]+x] += 1

m2 = 0

for item in gameGrid:
    for number in item:
        if number > 1:
            m2 += 1

print(m2)