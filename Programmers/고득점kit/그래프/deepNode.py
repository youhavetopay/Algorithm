from collections import deque

def solution(n, edge):
    answer = 0
    
    
    graph = {}
    
    for e in edge:
        try:
            graph[e[0]].append(e[1])
        except KeyError:
            graph[e[0]] = [e[1]]
        
        try:
            graph[e[1]].append(e[0])
        except KeyError:
            graph[e[1]] = [e[0]]
            
    queue = deque([[1]])
    
    visitDict = {}
    
    mainDepth = 0

    depths = [9999999999] * (n)
    
    # BFS
    while list(queue) != []:
        nodes = queue.popleft()
        tempList= []        
        for node in nodes:
            depths[node-1] = min(mainDepth,depths[node-1])

            for nextNode in graph[node]:
                try:
                    temp = visitDict[nextNode] # 방문 및 담겨있는지 체크
                except KeyError:
                    tempList.append(nextNode)
                    visitDict[nextNode] = 1

        print(visitDict)
        print(depths)
        if tempList != []:
            queue.append(tempList)
        mainDepth += 1

    maxValue = max(depths)

    for i in depths:
        if maxValue == i:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))