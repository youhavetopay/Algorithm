from typing import List

import collections
import heapq, sys

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        
        '''
            나의 풀이
            시작점에서 목적지까지 최저 비용으로 이동하는 비용(단 이동 제한 있음)을 반환하는 문제

            다익스트라에서 조금 응용하면 됨
            743.NetworkDelayTime 이 문제 풀이에서 약간 변형함

            BFS를 하는데 queue에 현재 이동 횟수를 넣어서 체크하는 방식으로 구현함
            한번 다익스트라 문제를 풀어서 그렇게 어렵지 않았음 ㅎㅎ
            
            많이 발전했다 !! ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            재밌다 알고리즘!!ㅋㅋㅋㅋ

        '''

        graph = collections.defaultdict(list)

        for start, end, price in flights:
            graph[start].append([end, price])
    

        price_table = [float('inf')] * n
        queue = collections.deque([[src, 0, 0]])

        while queue:
            now_loc, now_price, now_move = queue.popleft()

            if now_move <= k+1:
                price_table[now_loc] = min(price_table[now_loc], now_price)

            for next, price in graph[now_loc]:

                if now_move <= k+1 and now_price + price <= price_table[next]:
                    queue.append([next, now_price + price, now_move + 1])

        if price_table[dst] == float('inf'):
            return -1

        return price_table[dst]




    
    def firstSoul(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        '''
            책 풀이
            이거 타임아웃 뜸.. ㅋㅋㅋ
            깃허브에 확인해보니 테스트케이스 추가로 타임아웃 뜨는 듯함
            책에서는 다익스트라를 살짝 변형한 알고리즘이라고 하지만 
            중복탐색이 발생한다고 함

            뭐 어찌됬든 코드 읽기에는 참 깔끔한듯..
        '''

        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, k)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1
    
    def secondSoul(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        '''
            책 풀이 개선 코드(깃허브)

            나랑 비슷하게 비용 테이블?? 을 따로 만들어서
            갱신하는 방식으로 구현함

            근데 특이하기 sys.maxsize라는 걸로 float('inf') 대신하는듯??
            두개의 차이점을 찾아봤는데 알고리즘 풀이 때 큰 차이는 없는듯함
            maxsize는 숫자가 나오고 inf는 inf 라는 객체??? 가 나온다는 차이 정도??

            대충 999999999999 이런 숫자로 초기화 안하면 된다고 함 ㅋㅋㅋㅋ
        '''


        graph = collections.defaultdict(list)
        weight = [(sys.maxsize, k)] * n
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, k)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < weight[v][0] or k-1 >= weight[v][1]:
                        weight[v] = (alt, k-1)
                        heapq.heappush(Q, (alt, v, k - 1))
        return -1


obj = Solution()
print(obj.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))