좌표정렬하기

import sys
from collections import defaultdict

input = sys.stdin.readline

locCount = int(input().strip())

locations = defaultdict(list)

for i in range(locCount):
    x, y = map(int, input().strip().split())

    if locations[y] == None:
        locations[y] = x
    else:
        locations[y].append(x)

for y in sorted(list(locations.keys())):
    if len(locations[y]) > 1:
        for x in sorted(locations[y]):
            print(x, y)
    else:
        print(locations[y][0], y)