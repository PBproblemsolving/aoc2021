from collections import defaultdict
import math
import heapq


def relax(u, v, distances, vertices):
    if distances[v] > u + vertices[v]:
        distances[v] = u + vertices[v]

def increase(what, howmuch):
    if what + howmuch <= 9:
        return what + howmuch
    else:
        return what + howmuch - 9

def increment(y, x, yMAX, xMAX):
    return ((y // yMAX, x // xMAX), y // yMAX + x // xMAX)

with open('input15') as f:
    vertices = {}
    distances = {}
    f = f.readlines()
    f = [line[:-1] for line in f]

    newf = []
    for y in range(5):
        for line in f:
            newline = []
            for x in range(5):
                for number in line:
                    newline.append(increase(int(number), y + x))
            newf.append(newline)
    for y in range(len(newf)):
        for x in range(len(newf[0])):
            vertices[(x, y)] = newf[y][x]
            distances[(x, y)] = math.inf

xMAX = len(newf[0]) -1
yMAX = len(newf) -1

adj = defaultdict(list)
for v in vertices:
    for y in range(-1, 2, 1):
        for x in range(-1, 2, 1):
            if (y == 0 and x == 0) or v[0] + x > xMAX or v[0] + x < 0 \
             or v[1] + y > yMAX or v[1] + y < 0 or (abs(y) == abs(x)):
                pass
            else:
                adj[v].append((v[0]+x, v[1]+y))
    adj[v] = tuple(adj[v])

vertices[(0, 0)] = 0
distances[(0, 0)] = 0
to_visit = []
heapq.heapify(to_visit)
heapq.heappush(to_visit, (0, (0, 0)))
visited = set()

while to_visit:
    current = heapq.heappop(to_visit)
    if current[1] in visited:
        continue
    visited.add(current[1])
    children = adj[current[1]]
    for child in children:
        relax(current[0], child, distances, vertices)
        heapq.heappush(to_visit, (distances[child], child))


print(distances[(xMAX, yMAX)])