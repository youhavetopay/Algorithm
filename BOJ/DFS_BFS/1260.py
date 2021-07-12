# DFS와 BFS

def DFS(v):
    visit = [0] * (N+1)

    stack = [v]
    answer = []
    while stack != []:
        now = stack[-1]
        visit[now] = 1
        if now not in answer:
            answer.append(now)
        
        try:
            for i in graph[now]:
                if i not in stack and visit[i] != 1:
                    stack.append(i)
                    break
            else:
                stack.pop()
        except KeyError:
            answer = [v]
            return answer
    
    return answer
        

def BFS(v):
    visit = [0] * (N+1)
    answer = []
    queue = [v]

    while queue != []:
        now = queue.pop(0)
        
        try:
            for i in graph[now]:
                if visit[i] != 1 and i not in queue:
                    queue.append(i)
            answer.append(now)
            visit[now] = 1
        except KeyError:
            answer = [v]
            return answer

    return answer

N, M, V = map(int, input().split())

graph = {}

for i in range(M):
    start, end = map(int, input().split())

    try:
        graph[start].append(end)
        graph[start].sort()
    
    except KeyError:
        graph[start] = [end]

    try:
        graph[end].append(start)
        graph[end].sort()
    except KeyError:
        graph[end] = [start]

for i in DFS(V):
    print(i, end=' ')
print()
for i in BFS(V):
    print(i, end=' ')
    