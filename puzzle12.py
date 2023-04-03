from collections import defaultdict


def step(enter, connections_dict, routes, route = None):

    outputs = connections_dict.get(enter)
    for output in outputs:
        if route is None:
            route = []
        route = route[:]

        try:
            if output in route and output.islower():
                raise TypeError
            if output == 'end':
                if route == [] or route[-1] != enter:
                    route.append(enter)
                routes.append(route + ['end'])
            else:    
                try:
                    if route == [] or route[-1] != enter:
                        route.append(enter)
                    else:
                        pass
                    step(output, connections_dict, routes, route)
                except TypeError:
                    pass
        except TypeError:
            pass

def step2(enter, connections_dict, routes, route = None):

    outputs = connections_dict.get(enter)
    for output in outputs:
        if route is None:
            route = []
        route = route[:]

        try:
            if output == 'start':
                raise TypeError
            elif output == 'end':
                if route == [] or route[-1] != enter:
                    route.append(enter)
                routes.append(route + ['end'])
            elif output.islower() and route.count(output) > 1:
                raise TypeError
            else:
                if output.islower() and output in route:
                    lowers = [x for x in route if x.islower()]
                    for low in lowers:
                        if route.count(low) > 1:
                            raise TypeError    
                try:
                    if route == [] or route[-1] != enter:
                        route.append(enter)
                    else:
                        pass
                    step2(output, connections_dict, routes, route)
                except TypeError:
                    pass
        except TypeError:
            pass





def run(filename):
    list0 = defaultdict(list)

    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split('-')
            list0[line[0]].append(line[1])
            list0[line[1]].append(line[0])

    routes = []
    routes2 = []
    
    step('start', list0, routes)
    step2('start', list0, routes2)

    print(len(routes))
    print(len(routes2))
    print('\n')
    overprogram = 0
    for route in routes2:
        counter = 0
        lowers = [x for x in route if x.islower()]
        for low in lowers:
            if route.count(low) > 1:
                counter += 1
        if counter > 2:
            overprogram += 1
            print(counter)
    print(len(routes2) - overprogram)

# run('input121')
# run('input122')
# run('input123')
run('input12')





# with open('test12.txt') as test:
#     testlines = []
#     for line in test:
#         testlines.append(line.rstrip())

# test2lines = [','.join(x) for x in routes2]

# for test2line in test2lines:
#     if test2line not in testlines:
#         print(test2line)

