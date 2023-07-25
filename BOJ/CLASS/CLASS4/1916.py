
'''
    백준 1916. 최소비용 구하기

    방향 있는 그래프에서 다익스트라 하는 문제
'''

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
M = int(input())

bus_info = [list(map(int, input().split())) for _ in range(M)]

start, end = map(int, input().split())


def solution(n, bus_info, my_loc, target):

    '''
        나의 풀이

        나의 접근법

        내가 알고 있던 다익스트라는 다익스트라가 아니였음 ㅋㅋㅋㅋㅋ
        그것 때문에 한참 걸림 ㅋㅋ

        문제 보고 바로 다익스트라 라고 생각해서 했는데 시간초과 떠서
        이것저것 해보다가 인터넷에 다익스트라 검색하니까

        다음 탐색할 노드를 고르는게 
        현재 비용 테이블에서 가장 비용이 낮고 방문하지 않은 곳을 방문하는 거였음 ㅋㅋ
    '''

    if my_loc == target:
        return 0

    costs = [float('inf')] * (n + 1)

    costs[my_loc] = 0

    graph = defaultdict(list)

    for start, end, cost in bus_info:
        graph[start].append([end, cost])

    queue = deque()
    queue.append([my_loc, 0])
    visited = set()
    visited.add(my_loc)
    visited.add(0)

    while queue:

        now, now_cost = queue.popleft()

        for next, next_cost in graph[now]:
            total_next_cost = now_cost + next_cost
            if total_next_cost < costs[next]:
                costs[next] = total_next_cost
            
        temp = []
        for i, cost in enumerate(costs):
            temp.append([i, cost])
        
        temp.sort(key=lambda x:x[1])

        for i in range(len(temp)):
            if temp[i][0] not in visited:
                visited.add(temp[i][0])
                queue.append([temp[i][0], temp[i][1]])
                break
        
    return costs[target]

print(solution(N, bus_info, start, end))


import heapq

def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-1916-%EC%B5%9C%EC%86%8C%EB%B9%84%EC%9A%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python

        엥? 현재 연결된 노드에서 갱신된 곳으로 
        다음 탐색을 이어감

        다시 보니까
        힙에 들어갔다고 해서 해당 값이 무조건 최저 값이라는 보장이 없기에
        -> 들어가고 나서 새롭게 갱신될 수 있음

        그래서 최저값이 아닌게 힙에서 나오면 continue로 넘어가야함
        안그럼 시간 초과뜸
    '''
    
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    visited = [sys.maxsize] * (n + 1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, a))
    
    start, end = map(int, input().split())

    def dijkstra(x):
        pq = []

        heapq.heappush(pq, (0, x))
        visited[x] = 0

        while pq:
            d, x = heapq.heappop(pq)

            if visited[x] < d:
                continue

            for nw, nx in graph[x]:
                nd = d + nw
                
                if visited[nx] > nd:
                    heapq.heappush(pq, (nd, nx))
                    visited[nx] = nd

    dijkstra(start)
    print(visited[end])













import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    start, end, cost = list(map(int, input().split()))
    graph[start].append([end, cost])

my_start, target = map(int, input().split())

def solution2(n, graph, my_loc, target):

    '''
        나의 두번째 풀이

        맨 처음 했던 내가 알고 있던 다익스트라 알고리즘에
        continue 넣어줌

        그러니까 통과함 ㅋㅋㅋㅋ
        
    '''

    costs = [sys.maxsize] * (n + 1)

    costs[my_loc] = 0

    queue = deque()
    queue.append([my_loc, 0])

    while queue:

        now, now_cost = queue.popleft()

        if costs[now] < now_cost:
            continue

        for next, next_cost in graph[now]:
            total_next_cost = now_cost + next_cost
            if total_next_cost < costs[next]:
                costs[next] = total_next_cost
                queue.append([next, total_next_cost])

    return costs[target]

print(solution(N, graph, my_start, target))