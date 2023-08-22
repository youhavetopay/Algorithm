
'''
    백준 1504. 특정한 최단 경로
    1번 정점에서 N번정점까지 가는데 특정 정점 2개를 거쳐서 가는 
    최단 경로를 계산하는 문제
'''

import sys
input = sys.stdin.readline

import heapq
from collections import defaultdict


def solution():

    '''
        나의 풀이

        나의 접근법
        최단 경로라고 하길래 다익스트라 사용하면 되겠다 라는 생각이 들었음

        그래서 푸는 방법에 대해 고민좀 했는데
        방문해야하는 정점이 무조건 2개 고정이라서
        다익스트라 3번만 하면 될 것 같아서
        해보니 통과 ㅎㅎ

        처음에 했을 땐 
        방문해야하는 정점 2개를 입력받는데 이걸 a, b 라고 하면
        1 -> a, a -> b, b -> N 이렇게 했는데 자꾸 틀렸다고 나왔음 ㅋㅋㅋ

        왜 틀렸는지 이유를 몰라서
        경로가 중복이 있어서 그런가 싶어서 그래프 구조도 바꿔보고 했는데 자꾸 틀리다고 나오길래
        질문하기 게시판을 통해서 반례를 봤는데

        1 -> b, b -> a -> a -> N 이렇게 가는 경우가 최단 경로인 경우도 있는걸 알았음 ㅋㅋㅋ

        그래서 두 방법중 최소 값으로 결정하는 방식으로 하니까 풀림ㅋㅋㅋ

        내가 반례를 너무 못찾는 것 같음....
        문제를 푸는 건 끈기 있게 푸는데 정답이라고 확신하는 코드에서
        저런 세세한 특정 케이스를 잘 못찾고 바로 그냥 게시판으로 찾아보는 것 같음..

        반례도 깊게 혼자서 생각해보는 습관을 기르는게 좋을 것 같음..

    '''

    N, E = map(int, input().split())

    graph = defaultdict(dict)

    # 그래프 만들기
    # 중복 경로가 있으면 거리 짧은 거만 남겨두기
    for _ in range(E):
        start, end, cost = map(int, input().split())

        if end in graph[start]:
            graph[start][end] = min(cost, graph[start][end])
        else:
            graph[start][end] = cost
        
        if start in graph[end]:
            graph[end][start] = min(cost, graph[end][start])
        else:
            graph[end][start] = cost
        

    
    need_a, need_b = map(int, input().split())

    # 각각의 정점에서 다익스트라 해주기
    start_dist = dijkstra(graph, 1, N)
    need_a_dist = dijkstra(graph, need_a, N)
    need_b_dist = dijkstra(graph, need_b, N)

    # 1. 1 -> a -> b -> N
    first = start_dist[need_a] + need_a_dist[need_b] + need_b_dist[N]

    # 2. 1 -> b -> a -> N
    second = start_dist[need_b] + need_b_dist[need_a] + need_a_dist[N]

    answer = min(first, second)

    if answer == float('inf'):
        print(-1)
        return

    print(answer)

    return

def dijkstra(graph, start, N):

    dist = [float('inf')] * (N + 1)
    dist[start] = 0

    heap = [(0, start)]

    while heap:

        now_dist, now = heapq.heappop(heap)

        if dist[now] < now_dist:
            continue

        for next in graph[now]:
            cost = graph[now][next]
            next_dist = now_dist + cost
            if dist[next] > next_dist:
                heapq.heappush(heap, (next_dist, next))
                dist[next] = next_dist
    
    return dist


solution()



def firstSolu():

    '''
        다른 사람 풀이
        https://bbbyung2.tistory.com/61

        나랑 똑같은 풀이 ㅋㅋㅋㅋ
    '''

    input = sys.stdin.readline
    INF = int(1e9)

    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    # 방향성 없는 그래프이므로 x, y일 때와 y, x일 때 모두 추가
    for _ in range(e):
        x, y, cost = map(int, input().split())
        graph[x].append((y, cost))
        graph[y].append((x, cost))


    def dijkstra(start):
        distance = [INF] * (v + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        # 반환값은 최단 거리 배열
        return distance


    v1, v2 = map(int, input().split())

    # 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
    original_distance = dijkstra(1)
    v1_distance = dijkstra(v1)
    v2_distance = dijkstra(v2)

    v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
    v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

    result = min(v1_path, v2_path)
    print(result if result < INF else -1)