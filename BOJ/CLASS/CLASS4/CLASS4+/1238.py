
'''
    백준 1238. 파티
    단방향 그래프에서 하나의 목적지에 대해 각각의 모든 정점의 출발지로 해서
    최단 거리의 비용이 가장 큰 값을 계산하는 문제
'''

import sys
input = sys.stdin.readline

from collections import defaultdict
import heapq

def solution():

    N, M, X = map(int, input().split())

    # N, M, X = 4, 8, 2
    # temp = [
    #     [1, 2, 4],
    #     [1, 3, 2],
    #     [1, 4, 7],
    #     [2, 1, 1],
    #     [2, 3, 5],
    #     [3, 1, 2],
    #     [3, 4, 4],
    #     [4, 2, 3]
    # ]

    graph = defaultdict(list)
    X -= 1
    
    for _ in range(M):

        # i, j, cost = temp[_]
        i, j, cost = map(int, input().split())
        i -= 1
        j -= 1

        graph[i].append([j, cost])

    total_costs = bfs(N, graph, X)

    for now in range(N):
        if now != X:
            
            now_costs = bfs(N, graph, now)
            total_costs[now] += now_costs[X]
    
    print(max(total_costs))

        


def bfs(node_count, graph, start):

    heap = []
    dists = [float('inf')] * node_count

    dists[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:

        dist, now = heapq.heappop(heap)

        if dists[now] > dist:
            continue

        for next, cost in graph[now]:
            next_dist = dist + cost
            if dists[next] > next_dist:
                dists[next] = next_dist
                heapq.heappush(heap, (next_dist, next))

    return dists
    
solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://nkw011.github.io/baekjoon/baekjoon-1238/

        역방향 그래프를 이용하면 다익스트라 두번 만에 끝낼 수 있음 ㄷㄷ
        ? -> X 로 가는 거(정방향 다익스트라)
        ? <- X 로 가는 거(역방향 다익스트라)

        역방향 그래프를 활용하면 특정 지점으로 가는 모든 정점들의 최단거리를 구할 수 있음 !!
    '''

    INF = 1e10
    def input(): return sys.stdin.readline().rstrip()

    def dijkstra(s, edge):
        dist = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (s, 0))

        while q:
            w, d = heapq.heappop(q)
            if dist[w] < d:
                continue

            for nxt, c in edge[w]:
                if dist[nxt] > d + c:
                    dist[nxt] = d + c
                    heapq.heappush(q, (nxt, d + c))
        
        return dist
    
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        reverse_graph[b].append((a, c))
    
    node2x = dijkstra(x, reverse_graph)
    x2node = dijkstra(x, graph)

    print(max([x2node[i] + node2x[i] for i in range(1, n + 1) if i != x]))