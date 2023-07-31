
'''
    백준 1753. 최단경로
    출발지점에서 다른지점까지 가능 최단 경로를 구하는 문제
'''

import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq


def solution():

    '''
        나의 풀이

        나의 접근법
        누가봐도 다익스트라 문제여서
        deque로 구현을 하니까 시간초과가 떴음..
        그래서 다익스트라 시간복잡도를 검색해서 봤는데
        V^2 이라고 해서 보니까 정점이 최대 2만개 이기 때문에 4억이 나옴 ㅋㅋㅋ

        그래서 어떻게 하지 하다가 힙으로 하면 괜찮을까?? 라는 생각을 가지고 있었는데
        다익스트라를 ElogE 로 할 수 있는 알고리즘이 힙으로 구현하는거라고 해서
        해보니 통과함 ㅋㅋ

        사실상 정답을 거의 보고 한거나 마찬가지임 ㅋㅋ
        그래도 앞으로 다익스트라 할때는 heap 사용하면 될듯
    '''

    V, E = map(int, input().split())
    K = int(input())
    graph = defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    dists = [float('inf')] * (V + 1)
    dists[K] = 0
    heap = []
    heapq.heappush(heap, (0, K))

    while heap:

        dist, now = heapq.heappop(heap)

        if dists[now] > dist:
            continue

        for next, weight in graph[now]:
            next_weight = dist + weight
            if dists[next] > next_weight:
                dists[next] = next_weight
                heapq.heappush(heap, (next_weight, next))

    for i in range(1, len(dists)):
        if dists[i] == float('inf'):
            print('INF')
        else:
            print(dists[i])


def firstSolu():

    '''
        다른 사람 풀이
        https://sungmin-joo.tistory.com/33

        나랑 풀이가 똑같음ㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    INF = sys.maxsize
    V, E = map(int, input().split())
    #시작점 K
    K = int(input())
    #가중치 테이블 dp
    dp = [INF]*(V+1)
    heap = []
    graph = [[] for _ in range(V + 1)]

    def Dijkstra(start):
        #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
        dp[start] = 0
        heapq.heappush(heap,(0, start))

        #힙에 원소가 없을 때 까지 반복.
        while heap:
            wei, now = heapq.heappop(heap)

            #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
            if dp[now] < wei:
                continue

            for w, next_node in graph[now]:
                #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
                # = 다음 노드까지의 가중치(next_wei)
                next_wei = w + wei
                #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
                if next_wei < dp[next_node]:
                    #계산했던 next_wei를 가중치 테이블에 업데이트.
                    dp[next_node] = next_wei
                    #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
                    heapq.heappush(heap,(next_wei,next_node))

    #초기화
    for _ in range(E):
        u, v, w = map(int, input().split())
        #(가중치, 목적지 노드) 형태로 저장
        graph[u].append((w, v))


    Dijkstra(K)
    for i in range(1,V+1):
        print("INF" if dp[i] == INF else dp[i])