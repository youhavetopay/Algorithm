
import sys
input = sys.stdin.readline

from collections import deque

count = int(input())

potato = list(map(int, input().split()))

potato.sort()

queue = deque(potato)

sung, park = 0, 0

while len(queue) > 1:

    park += queue.pop()
    sung += queue.popleft()

if queue:
    park += queue.pop()

print(sung, park)