# 1389 케빈 베이컨의 6단계 법칙

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split(' '))

    graph[A].append(B)
    graph[B].append(A)

def BFS(i):
    queue = deque()
    queue.append([i, 0])

    visit = [False] * (N+1)
    levels = [0] * (N+1)
    visit[i] = True
    while len(queue) != 0:
        info = queue.popleft()
        loc, level = info[0], info[1]
        levels[loc] = level

        for node in graph[loc]:
            if visit[node] == False:
                visit[node] = True
                queue.append([node, level+1])

    return sum(levels)

i = 1
answers = [0 for _ in range(N+1)]
while i <= N:
    answers[i] = BFS(i)
    i += 1

answer = 1000
min_value = 10000
for i, value in enumerate(answers):
    if i > 0:
        if value < min_value:
            answer = i
            min_value = value

print(answer)