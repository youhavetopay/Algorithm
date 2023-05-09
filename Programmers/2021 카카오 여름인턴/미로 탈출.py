import collections

def getGraph(roads):

    graph = collections.defaultdict(list)

    for start, end, cost in roads:
        graph[start].append([end, cost])

    return graph

def changeRoads(trap, new_roads):

    for i in range(len(new_roads)):
        start, end, cost = new_roads[i]
        if start == trap or end == trap:
            new_roads[i] = [end, start, cost]
    
    return new_roads

def getNewVisit(trap, new_roads, visit):

    for start, end, cost in new_roads:
        if trap in (start, end):
            visit[end] = 0

    return visit

def solution(n, start, end, roads, traps):

    '''
        나의 풀이 (못품.ㅜㅜㅜ)

        그래프를 탐색하는데 최소 비용을 구하는 문제
        단 함정에 도착하면 함정과 연결된 길은 방향이 반전이 됨..

        나의 접근법
        처음엔 DFS로 해볼려다가 답도 없어서
        BFS로 바꿨는데 방문 체크를 어떤식으로 해야
        중복 방문을 막을지 생각을 못하겠어서 결국 포기...ㅠㅠ
    '''

    traps = set(traps)

    queue = collections.deque()
    queue.append([start, roads[:], [0] * (n+1), 0])

    cost_table = [float('inf')] * (n + 1)
    cost_table[start] = 0

    count = 0

    while queue:
        print(queue)
        now, now_roads, now_visit, now_cost = queue.popleft()
        cost_table[now] = min(cost_table[now], now_cost)

        graph = getGraph(now_roads)

        for next, cost in graph[now]:
            if next == end:
                cost_table[end] = min(cost_table[end], now_cost + cost)
                break


            if now_visit[next] == 0:
                if next in traps:
                    change_road = changeRoads(next, now_roads[:])
                    next_visit = getNewVisit(next, change_road, now_visit[:])
                    next_visit[next] = 1
                    queue.append([next, change_road, next_visit, now_cost + cost])
                else:
                    now_visit[next] = 1
                    queue.append([next, now_roads, now_visit, now_cost + cost])
        
        count += 1
        if count > 10_000:
            break

    print(cost_table)

    return cost_table[end]

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))

import heapq as hq
import sys
INF = sys.maxsize

def firstSolu(n, start, end, roads, traps):

    '''
        다른 사람 풀이
        https://slowsure.tistory.com/137

        비트마스크에다 다익스트라...

        함정의 발동 여부를 비트마스크로 체크하면서
        함정들의 상태에 따른 방문 여부를 체크하는 방식으로 
        다익스트라 알고리즘으로 찾아가는 방식./????

        문제 자체가 너무 어려운듯.....ㅜㅜ
    '''

    answer = INF
    active = 0b0
    graph = [[] for _ in range(n+1)]
    visited = [[False for _ in range(2 ** len(traps) + 1)] for __ in range(n+1)]

    temp = {}

    for i in range(1, n+1):
        temp[i] = (False, 0)
    
    for t in traps:
        temp[t] = (True, traps.index(t))

    traps = temp

    for D, A, W in roads:
        ele = (A, W, True)
        graph[D].append(ele)
        ele = (D, W, False)

        graph[A].append(ele)
    
    que = [(0, start, active)]

    while que:
        weight, N, active = hq.heappop(que)

        if N == end:
            answer = min(answer, weight)

        if visited[N][active] is True:
            continue
        else:
            visited[N][active] = True

        N_is_trap = False
        if traps[N][0]:
            N_is_trap = True
            active = active ^ (1 << traps[N][1])
        
        for A, W, state in graph[N]:
            if N_is_trap and active & (1 << traps[N][1]) > 0:
                if traps[A][0] and active & (1 << traps[A][1]) > 0:
                    if state is True:
                        ele = (W + weight, A, active)
                        hq.heappush(que, ele)
                
                elif state is False:
                    ele = (W + weight, A, active)
                    hq.heappush(que, ele)
            
            else:

                if traps[A][0] and active & (1 << traps[A][1]) > 0:
                    if state is False:
                        ele = (W + weight, A, active)
                        hq.heappush(que, ele)
                elif state is True:
                    ele = (W + weight, A, active)
                    hq.heappush(que, ele)
        
    return answer