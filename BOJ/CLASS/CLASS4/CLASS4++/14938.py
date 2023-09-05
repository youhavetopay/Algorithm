
'''
    백준 14938. 서강그라운드
    내가 갈 수 있는 거리에서 얻을 수 있는 최대 아이템 갯수를 구하는 문제
'''

import sys
input = sys.stdin.readline

def solution():

    '''
        나의 풀이

        나의 접근법
        하나의 정점에서 시작해서 돌아오는 거리는 생각안하고
        가는 거리만 따지기 때문에 최단거리 문제였음

        그리고 어느 정점에서 제일 많은 정점을 방문해야해서
        모든 정점에서의 각각의 최단거리를 구하는 플로이드워셜을 떠올리게 되었음

        정점개수도 100개라서 충분히 n^3 안으로 가능할 것 같아서 해보니 통과함 ㅎㅎ

        플로이드 워셜을 알고 있다면 쉽게 쉽게 풀 수 있는듯 함
    '''

    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))

    load = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        load[i][i] = 0


    for _ in range(r):
        start, end, cost = map(int, input().split())
        start -= 1
        end -= 1

        load[start][end] = min(load[start][end], cost)
        load[end][start] = min(load[end][start], cost)
    
    

    for waypoint in range(n):
        for start in range(n):
            for end in range(n):
                load[start][end] = min(load[start][waypoint] + load[waypoint][end], load[start][end])
    
    max_item = 0
    for row in load:
        now_item = 0
        for i in range(n):
            if row[i] <= m:
                now_item += items[i]
        
        max_item = max(max_item, now_item)

    print(max_item)

solution()


import heapq

def firstSolu():

    '''
        다른 사람 풀이
        https://donghak-dev.tistory.com/86

        다익스트라를 N 번 해서 풀어낸 방법도 있음
        
        n^3 이나 n*2*logN 이나 비슷할듯 ??? ㅋㅋㅋㅋㅋ
        아님 이게 좀더 빠를듯?? ㅋㅋㅋ
    '''

    N, M, R = map(int, input().split())

    area_item = list(map(int, input().split()))
    area_item.insert(0, 0)

    arr = [ [] for _ in range(N+1)]

    def dijkstra(S):
        Q = []
        distance = [sys.maxsize] * (N + 1)

        heapq.heappush(Q, [0, S])
        distance[S] = 0

        while Q:
            now_dist, now_vertex = heapq.heappop(Q)

            for next_dist, next_vertex in arr[now_vertex]:
                if next_dist + now_dist < distance[next_vertex]:
                    next_dist += now_dist
                    distance[next_vertex] = next_dist
                    heapq.heappush(Q, [next_dist, next_vertex])
            
        
        return distance

    
    for _ in range(R):
        start, end, dist = map(int, input().split())
        arr[start].append([dist, end])
        arr[end].append([dist, start])
    
    max_value = int(-1e9)

    for i in range(1, N+1):
        temp_sum = 0
        result = dijkstra(i)

        for j in range(1, N+1):
            if result[j] <= M:
                temp_sum += area_item[j]
        
        max_value = max(max_value, temp_sum)
    
    print(max_value)