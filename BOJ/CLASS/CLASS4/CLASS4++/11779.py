
'''
    백준 11779. 최소비용 구하기2
    방향 있는 그래프에서 A->B 로 가는 최소 비용과 루트를 구하는 문제
'''

import sys
import heapq
input = sys.stdin.readline


def solution():

    '''
        나의 풀이

        처음엔 문제를 제대로 안읽고 플로이드워셜로 풀어보려고 했으나
        최소비용만 구하는게 아니라 최단 경로 까지 구해야하는 문제라는 걸 께닫고
        다른 방법을 생각하게됨

        그래서 DFS로 탐색을 하면서 최단 거리를 갱신하는 방식으로 풀었는데
        당연히 시간초과 ㅋㅋㅋ

        어쩌지 하고 있다가 결국 알고리즘 분류를 봤는데
        다익스트라 라고 되어 있어서 여기에 힌트를 얻어서
        다익스트라를 진행하면서 최단 경로를 구하는 방식으로 했더니 
        3%에서 자꾸 틀렸다고 나오길래 질문하기 게시판을 좀 살펴봄

        질문하기의 반례들을 살펴보다가 내 코드에서 이상한 점을 발견함
        최소 비용은 잘 구하고 있는데 보니까 최단 경로는 방문 노드에 상관 없이 계속 업데이트를 하고 있었음
        그래서 최단 거리도 목적지에 따라 다르게 하도록 2차원 배열에 넣어주고 해줬더니 통과...

        정말 오랜만에 알고리즘 문제를 풀어서 그런지 문제를 보고
        바로 다익스트라를 생각하지 못했음...
        그리고 이상한 헛짓을 많이 한듯..
        앞으로 다시 꾸준히 열심히 하자..!!!
    '''

    n = int(input())
    m = int(input())

    graph = [[float('inf')] * n for _ in range(n)]

    for _ in range(m):
        start, end, cost = map(int, input().split())
        start -= 1
        end -= 1
        graph[start][end] = min(graph[start][end], cost)

    start, end = map(int, input().split())



    # n = 5
    # m = 8

    # graph = [[float('inf')] * n for _ in range(n)]

    # temp = [
    #     [1, 2, 2],
    #     [1, 3, 3],
    #     [1, 4, 1],
    #     [1, 5, 10],
    #     [2, 4, 2],
    #     [3, 4, 1],
    #     [3, 5, 1],
    #     [4, 5, 3]
    # ]

    # for _ in range(m):
    #     start, end, cost = temp[_]
    #     start -= 1
    #     end -= 1

    #     graph[start][end] = min(graph[start][end], cost)
    
    
    # start, end = 1, 5


    start -= 1
    end -= 1

    costs = [float('inf')] * n
    heap = [[0, start, [start+1]]]
    min_load = [[start+1] for _ in range(n)]
    costs[start] = 0

    while heap:
        
        now_cost, now, load = heapq.heappop(heap)

        if now_cost > costs[now]:
            continue

        for next, cost in enumerate(graph[now]):
            next_cost = now_cost + cost
            if next_cost < costs[next] and next+1 not in load:
                costs[next] = next_cost
                min_load[next] = load + [next+1]
                heapq.heappush(heap, [next_cost, next, load + [next+1]])
    

    print(costs[end])
    print(len(min_load[end]))
    print(*min_load[end])
        


solution()



import sys
from collections import defaultdict
import heapq

INF = int(1e9)

def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@yoopark/baekjoon-11779

        똑같이 다익스트라로 풀었으나
        경로를 구하는 부분에 있어서 다름

        비용을 갱신하면서 해당 비용의 경로를 배열에 기록
        그 후 목적지에서 출발지까지 거슬러 올라가면서 경로를 찾은 다음
        뒤집어줌 

        경로 찾는 부분에 있어서 나보다 훨~~~~~~~~~씬 효율적인듯. ㅋㅋㅋㅋ
    '''

    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    graph = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append((b, c))
    
    start, end = map(int, sys.stdin.readline().rstrip().split())

    dist = [INF] * (n + 1)
    prev_node = [0] * (n + 1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0

        while q:
            weight, node = heapq.heappop(q)
            if dist[node] < weight:
                continue

            for adj_node, adj_weight in graph[node]:
                cost = weight + adj_weight
                if cost < dist[adj_node]:
                    dist[adj_node] = cost
                    prev_node[adj_node] = node
                    heapq.heappush(q, (cost, adj_node))
        
    dijkstra(start)
    print(dist[end])

    path = [end]
    now = end
    while now != start:
        now = prev_node[now]
        path.append(now)
    
    path.reverse()

    print(len(path))
    print(' '.join(map(str, path)))