
'''
    백준 11404. 플로이드
    단방향 그래프에서 모든 정점에서의 최단 거리를 구하는 문제
'''

import sys
input = sys.stdin.readline

def solution():

    '''
        나의 풀이

        나의 접근법
        딱 봐도 플로이드 워셜 문제라서 해봤는데
        문제는 내가 플로이드 워셜를 할줄 모른다는 거 였음 ㅋㅋ
        대충 경유지 거처서 가는거랑 비교하는 걸로 알고 있고 3중 for 문이라는 것도 알지만
        자세한 내용을 몰라서 결국 알고리즘을 보고 품 ㅋㅋ

        사용안하면 자꾸 까먹어서 한번 알고리즘에 대해 정리해두는게 좋을 듯 함
    '''

    n = int(input())
    m = int(input())

    costs = [[sys.maxsize] * n for _ in range(n)]

    for _ in range(m):
        i, j, cost = map(int, input().split())

        i -= 1
        j -= 1

        costs[i][j] = min(costs[i][j], cost)
    
    for waypoint in range(n):
        for start in range(n):
            for end in range(n):
                if start == end:
                    costs[start][end] = 0

                if start == end or start == waypoint or end == waypoint:
                    continue

                waypoint_dists = costs[start][waypoint] + costs[waypoint][end]
                if costs[start][end] > waypoint_dists:
                    costs[start][end] = waypoint_dists
                    
    for y, row in enumerate(costs):
        for x in range(n):
            if costs[y][x] == sys.maxsize:
                costs[y][x] = 0
        print(*row)

solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://ryu-e.tistory.com/106

        나랑 똑같이 플로이드 워셜로 하심

        플로이드 워셜 점화식이
        dp[start][end] = min(dp[start][end], dp[start][waypoint] + dp[waypoint][end]) 
        인걸 꼭 기억하자

        그리고 플로이드 워셜이 다이나믹 프로그래밍 유형이라고 함
        다익스트라는 그리디?? ㅋㅋ
    '''

    INF = int(1e9)

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a][b] = min(c, graph[a][b])

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print('0', end = ' ')
            else:
                print(graph[a][b], end = " ")
        
        print()