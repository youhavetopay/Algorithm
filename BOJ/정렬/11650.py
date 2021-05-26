# 좌표정렬하기

import sys
from collections import defaultdict
input = sys.stdin.readline

locCount = int(input())

locations = defaultdict(list)

for i in range(locCount):
    x,y = map(int, input().strip().split())

    if locations[x] == None:
        locations[x] = y
    else:
        locations[x].append(y)

for x in sorted(list(locations.keys())):
    if len(locations[x]) > 1:
        for y in sorted(locations[x]):
            print(x, y)
    else:
        print(x, locations[x][0])