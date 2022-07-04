from collections import defaultdict, deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split(' '))


graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split(' '))

    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visit_nodes = [False] * N
queue = deque([0])

answer = 1

while True:

    while len(queue) != 0:
        now_node = queue.popleft()

        visit_nodes[now_node] = True

        for node in graph[now_node]:
            if (not visit_nodes[node]) and (node not in queue):
                queue.append(node)

    
    for i, visit in enumerate(visit_nodes):
        if not visit:
            queue.append(i)
            answer += 1
            break
    
    if len(queue) == 0:
        break

print(answer)