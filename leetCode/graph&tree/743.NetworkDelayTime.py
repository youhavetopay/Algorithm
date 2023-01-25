from typing import List

import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        '''
            나의 풀이
            특정한 지점에서의 노드별 최단거리의 최대값을 반환하는 문제
            (엣지에 가중치 있고 방향도 있음)

            이거 다익스트라로 하는건가???

            일단 나는 타임테이블 만들어놓고
            BFS로 탐색을 시작
            현재까지의 시간과 현재 연결된 정점과의 시간을 더한 값 보다
            타임테이블 값이 크면 queue에 담고 탐색을 하는 방법으로 구현함

            만약 타임테이블 최대값이 INF 이거나 연결정보가 없으면 -1을 반환하는 방식으로 함
        '''

        graph = collections.defaultdict(list)

        for start, end, time in times:
            graph[start].append([end, time])

        if k not in graph:
            return -1
        
        time_table = {}
        for i in range(1, n+1):
            time_table[i] = float("inf")

        queue = collections.deque()
        queue.append([k, 0])

        while queue:
            now_loc, now_time = queue.popleft()
            time_table[now_loc] = min(now_time, time_table[now_loc])
        
            for end, time in graph[now_loc]:
                if now_time+time < time_table[end]:
                    queue.append([end, now_time+time])

        max_time = max(time_table.values())
        if max_time == float('inf'):
            return -1

        return max_time
    
    def firstSoul(self, times: List[List[int]], n: int, k: int) -> int:

        '''
            책 풀이
            다익스트라 알고리즘을 사용함
            대신 우선순위 큐를 사용하기 위해 heapq를 사용함

            heapq를 사용하면 거리가 가장 짧을거 부터 나오기 때문에
            그렇게 한듯??

            풀이는 전체적으로 나랑 비슷함..
            근데 heapq를 사용해서 좀더 빠른듯??
            그리고 heapq를 사용해서 min 을 계속 안해주는게 가장 큰듯??
            내꺼는 810ms이고 이거는 680ms

        '''

        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append([v, w])
        
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)

            if node not in dist:
                dist[node] = time

                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        if len(dist) == n:
            return max(dist.values())

        return -1
    
obj = Solution()
print(obj.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))

print(obj.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1))