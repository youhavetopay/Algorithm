
'''
    프로그래머스 배달
    1번마을에서 거리가 K 이하인 마을의 개수를 구하는 문제
'''


from collections import deque, defaultdict

def solution(N, road, K):

    '''
        나의 풀이

        나의 접근법
        그냥 다익스트라로 최단거리 구하고
        체크하는 방식으로 품

        1번 마을도 K 거리 이하여서 이것도 포함해야하는지 모르고
        왜 틀리지 이 생각함 ㅋㅋㅋㅋ
    '''

    answer = 1

    graph = defaultdict(list)

    for start, end, cost in road:
        graph[start].append([end, cost])
        graph[end].append([start, cost])
    
    queue = deque()
    dists = [float('inf')] * (N + 1)
    dists[1] = 0
    queue.append([1, 0])

    while queue:

        now, now_cost = queue.popleft()

        if now_cost > dists[now]:
            continue

        for next, dist in graph[now]:
            next_cost = now_cost + dist
            if dists[next] > next_cost:
                dists[next] = next_cost
                queue.append([next, next_cost])

    print(dists)

    for i in range(2, len(dists)):
        if dists[i] <= K:
            answer += 1

    return answer

print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))

import heapq

def dijkstra(dist, adj):

    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap, [cost + c, n])

def firstSolu(N, road, K):

    '''
        다른 사람 풀이
        https://jennnn.tistory.com/83

        나랑 똑같이 다익스트라 사용해서 푸심
        대신 heap을 사용해서 좀 더 깔끔한듯??
    '''

    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    adj = [[] for _ in range(N+1)]

    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])
    

    dijkstra[dist, adj]
    return len([i for i in dist if i <= K])