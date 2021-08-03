graph =[
    [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visit = [False] * len(graph)

def DFS(i):
    global visit
    visit[i] = True
    print(i,end=" ")

    for node in graph[i]:
        if not visit[node]:
            DFS(node)


DFS(1)
print()
visit2 = [False] * len(graph)
queue = []

def BFS(i):   
    global visit2, queue
    visit2[i] = True
    print(i,end=" ")

    for node in graph[i]:
        if not visit2[node] and node not in queue:
            queue.append(node)
    
    if queue == []:
        return
    else:
        BFS(queue.pop(0))

def BFS2(i):   
    global visit2
    visit2[i] = True
    print(i,end=" ")
    nextLoc = i
    
    while True:
        for node in graph[nextLoc]:
            if not visit2[node] and node not in queue:
                queue.append(node)
        
        if queue == []:
            return
        
        nextLoc = queue.pop(0)
        visit2[nextLoc] = True
        print(nextLoc,end=" ")

    
    
BFS(1)
print()
visit2 = [False] * len(graph)
queue = []
BFS2(1)