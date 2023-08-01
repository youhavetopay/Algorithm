
'''
    백준 1967. 트리의 지름
    트리에서 두 정점을 이어주는 길의 비용이 최대인
    비용을 구하는 문제
'''

import sys
from collections import deque
import heapq
input = sys.stdin.readline


def solution():

    '''
        나의 풀이

        나의 접근법
        처음에 그냥 각 정점에서 BFS 한번씩 해주고 최대 비용을 구하려고 했는데
        메모리 초과가 떴었음 ㅋㅋㅋㅋ

        그래서 메모리 줄여볼려고 이것저것 해보다가 
        굳이 2차원 배열에 비용을 기록할 필요가 없는 것 같아서 지우니까
        이번엔 시간초과가 떴음 ㅋㅋㅋ

        그래서 다시 생각해봤는데
        일단 루트에서 한번 BFS 를 해서 거리를 구한 다음
        거리값의 최대값 두개를 뽑아서 해볼려고 했는데 틀렸습니다가 떴음 ㅋㅋㅋ

        그러다가 루트에서 가장 비용이 큰 노드를 구한 다음 해당 노드에서
        다시 BFS를 해서 최대 비용을 찾아주면 되는 거였음 ㅋㅋㅋㅋ

        풀고보면 간단한 문제인데 좀 힘들었음 ㅁㅋㅋㅋ
    '''

    # N = int(input())
    # graph = [
    #     [] * N
    # ]

    # for _ in range(N-1):
    #     u, v, w = map(int, input().split())
    #     u -= 1
    #     v -= 1
    #     graph[u].append([v, w])
    #     graph[v].append([u, w])

    N = 1
    graph = [
        [] for _ in range(N)
    ]

    load = [
        
        [1, 6, 7],
        
    ]

    for _ in range(N-1):
        u, v, w = load[_]
        u -= 1
        v -= 1
        graph[u].append([v, w])
        graph[v].append([u, w])


    def get_dists(start, graph):

        queue = deque()
        queue.append([start, 0])
        
        dist = [0] * len(graph)
        dist[start] = -1

        while queue:

            now, d = queue.popleft()

            for next, weight in graph[now]:
                if dist[next] == 0:
                    dist[next] = d + weight
                    queue.append([next, d + weight])
        
        return dist

    answer = 0

    if N > 1:
        dists = get_dists(0, graph)
        dists[0] = 0

        heap = [(-dist, i) for i, dist in enumerate(dists)]
        heapq.heapify(heap)
        left = heapq.heappop(heap)

        left_dist = get_dists(left[1], graph)
        answer = max(left_dist)

    print(answer)

sys.setrecursionlimit(10**9)
def firstSolu():

    '''
        다른 사람 풀이
        https://kyun2da.github.io/2021/05/04/tree's_diameter/

        나랑 똑같이 루트에서 거리를 계산하고
        그 거리중 가장 먼곳에서 다시 거리계산을 하는 방식으로 하심

        DFS 로 하니까 코드가 짧아서 그런지 좀 더 깔끔한듯??
    '''

    n = int(input())
    graph = [[] for _ in range(n + 1)]

    def dfs(x, wei):
        for i in graph[x]:
            a, b = i
            if distance[a] == -1:
                distance[a] = wei + b
                dfs(a, wei + b)
    
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    distance = [-1] * (n + 1)
    distance[1] = 0
    dfs(1, 0)

    start = distance.index(max(distance))
    distance = [-1] * (n + 1)
    distance[start] = 0

    dfs(start, 0)

    print(max(distance))