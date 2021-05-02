# 바이러스 2606
from collections import defaultdict
computerCount = int(input())
count = int(input())
edges = []
for i in range(count):
    edges.append(list(map(int, input().split())))

graph = defaultdict(list)

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)
print(graph)
checkList = [False] * (computerCount + 1)
print(checkList)
stack = []
nowLocation = 1
answer = 0
while True:
    if checkList[nowLocation] != True:
        answer += 1
    checkList[nowLocation] = True
    print(nowLocation, ' 방문')
    for i in graph[nowLocation]:
        if checkList[i] == False:
            stack.append(i)
    if len(stack) == 0:
        break
    nowLocation = stack[-1]
    stack.pop()

print(answer-1)