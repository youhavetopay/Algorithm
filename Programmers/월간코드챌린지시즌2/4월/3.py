from collections import defaultdict
import sys
sys.setrecursionlimit(300000)
answer = 0
def solution(a, edges):
    global answer
    if sum(a) != 0:
        return -1

    graph = defaultdict(list)  # key value형식인데 중복 key값 들어오면 value에 추가하기 list로 하기

    print(graph2)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print(graph)

    def dfs(u,v):
        global answer
        for node in graph[u]:
            if node != v:
                dfs(node, u)
        answer += abs(a[u])
        a[v] += a[u]
        a[u] = 0

    dfs(0,0)

    return answer


a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
graph2 = {}

for u, v in edges:
    if graph2.get(u):
        graph2[u].append(v)
    else:
        graph2[u] = []
        graph2[u].append(v)
    if graph2.get(v):
        graph2[v].append(u)
    else:
        graph2[v] = []
        graph2[v].append(u)

def testDFS(graph2):
    stack = []
    checkList = [False] * len(a)

    nowLocation = 0
    while True:
        print(nowLocation, ' 의 값', a[nowLocation])
        checkList[nowLocation] = True
        checkValue = 0
        for value in graph2[nowLocation]:
            if checkList[value] == False:
                stack.append(value)
                checkValue = 1
        if checkValue == 0:
            print(nowLocation ,' 리프노드임')
        if len(stack) == 0:
            break
        nowLocation = stack[-1]
        stack.pop()

testDFS(graph2)
# print(solution(a, edges))