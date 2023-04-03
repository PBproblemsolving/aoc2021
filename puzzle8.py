def newdict():
    return {'0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
list0 = []

def diff(s1, s2):
    return len(set(s1)-set(s2))

with open('aoc2021/input8') as f:
    for line in f:
        line = line.rstrip('\n').split(' | ')
        line[0] = line[0].split()
        line[1] = line[1].split()
        list0.append(line)

ex = [2, 4, 3, 7]
counter = 0
output_int = 0

for line in list0:
    num_dict = newdict()
    #0, 6, 9
    sixths = []
    #2, 3, 5
    fifths = []
    for displayed in line[0]:
        if len(displayed) == 2:
            num_dict['1'] = displayed
        elif len(displayed) == 4:
            num_dict['4'] = displayed
        elif len(displayed) == 3:
            num_dict['7'] = displayed
        elif len(displayed) == 7:
            num_dict['8'] = displayed
        elif len(displayed) == 6:
            sixths.append(displayed)
        elif len(displayed) == 5:
            fifths.append(displayed)
    eg = diff(num_dict['8'],num_dict['7']+num_dict['4'])
    for item in sixths:
        if diff(num_dict['4'], item) == 0:
            num_dict['9'] = item
            sixths.remove(item)
    for item in sixths:
        if diff(num_dict['1'], item) == 0:
            num_dict['0'] = item
            sixths.remove(item)
    num_dict['6'] = sixths[0]
    c = set(num_dict['1']) - set(num_dict['6'])
    for item in fifths:
        if diff(num_dict['1'], item) == 0:
            num_dict['3'] = item
            fifths.remove(item)
    for item in fifths:
        if diff(item, c) == 4:
            num_dict['2'] = item
            fifths.remove(item)
    num_dict['5'] = fifths[0]
    output_string = ''
    for digit in line[1]:
        for key, value in num_dict.items():
            if sorted(value) == sorted(digit):
                output_string += key
    output_int += int(output_string)

print(output_int)

