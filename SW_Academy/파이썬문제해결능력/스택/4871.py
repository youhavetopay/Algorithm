T = int(input())

# 경로 찾기 DFS?
# a ~ b 까지 경로가 있는지

for test_case in range(1, T+1):
    
    V, E = map(int, input().split())

    graph = {}
    visitList = [False] * (V+1)

    for i in range(E):
        a, b = map(int, input().split())
        try:
            graph[a].append(b)
        except KeyError:
            graph[a] = [b]

        # 문제가 방향이 있는 그래프 라서 이거 아님 ㅋㅋ
        # try:
        #     graph[b].append(a)
        # except KeyError:
        #     graph[b] = [a]
    


    start, end = map(int, input().split())
    stack = [start]
    visitList[start] = True

    #print(graph)

    while stack:
        visitNode = stack.pop(0)
        visitList[visitNode] = True

        #print(visitList, stack, visitNode)

        if visitList[end]:
            break
    
        try:
            for node in graph[visitNode]:
                if not visitList[node]:
                    stack.append(node)
        except KeyError:
            continue
        #print('vsisvisvi ',visitList, stack, visitNode)

    if visitList[end]:
        answer = 1
        print("#{} {}".format(test_case, answer))
    else:
        answer = 0
        print("#{} {}".format(test_case, answer))