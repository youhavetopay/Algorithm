import math

A, B, V = map(int, input().split(' '))

total_day = math.ceil((V - A) / (A-B))

print(total_day + 1)
