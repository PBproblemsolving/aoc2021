def flash(y, x, oct_grid, flashed):
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1): 
            if y+i < 0 or y+i >= len(oct_grid) or x+j < 0 or x+j >= len(oct_grid[0]) or (j==0 and i==0):
                pass
            else:
                oct_grid[y+i][x+j] += 1
                if oct_grid[y+i][x+j] > 9 and (y+i,x+j) not in flashed:
                    flashed.append((y+i,x+j))
                    flash(y+i, x+j, oct_grid, flashed)

list0= []

with open('input11') as f:
    for line in f:
        line = list(line.rstrip('\n'))
        for index, _ in enumerate(line):
            line[index] = int(line[index])
        list0.append(line)

column_len = len(list0)
row_len = len(list0[0])
flashes = 0 

for i in range(1000):
    flashed = []
    for y in range(column_len):
        for x in range(row_len):
            list0[y][x] += 1
    for y in range(column_len):
        for x in range(row_len):
            if list0[y][x] > 9 and (y,x) not in flashed:
                flashed.append((y,x))
                flash(y, x, list0, flashed)
    for y in range(column_len):
        for x in range(row_len):
            if list0[y][x] > 9:
                list0[y][x] = 0
                flashes += 1
    if i == 99:
        print(flashes)
    if len(flashed) == len(list0)*len(list0[0]):
        print(i+1)
        break
        

