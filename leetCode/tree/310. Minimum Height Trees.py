from typing import List


import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        '''
            나의 풀이
            연결정보가 주어졌을 때 트리에서 어떤 노드를 루트로 삼았을 때
            최대 깊이가 제일 작은지 반환하는 문제

            못품... 68번 TC에서 시간초과 뜸

            먼저 그래프를 만들고
            번호 순서대로 DFS 시작
            노드의 최대 깊이를 따로 저장해두고
            탐색 중 최대 깊이를 넘어가면 컷 하는 방식으로 구현

            근데 시간초과 뜸..
            단순 탐색으로 풀리는 문제가 아닌가..??
        '''

        if len(edges) == 0:
            return [0]

        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        short_roots = []

        total_min_depth = float('inf')
        

        for start_node in range(n):

            visit = set()
            visit.add(start_node)
            
            stack = [start_node]
            depth = 0
            now_max_depth = 0

            while stack:
                
                if now_max_depth > total_min_depth:
                    break

                for next in graph[stack[-1]]:
                    if next not in visit:
                        visit.add(next)

                        depth += 1
                        now_max_depth = max(depth, now_max_depth)
                        stack.append(next)

                        break

                else:
                    depth -= 1
                    stack.pop()
            

            if now_max_depth < total_min_depth:
                total_min_depth = now_max_depth
                short_roots = [start_node]
            elif now_max_depth == total_min_depth:
                short_roots.append(start_node)

        

        return short_roots
    
    def firstSoul(self, n: int, edges: List[List[int]]) -> List[int]:

        '''
            책 풀이
            리프노드를 계속 제거하는 방식으로 구현...ㄷㄷ
            
            최소 높이를 구성하려면 가장 가운데..?? 있는 값이 루트이어야 한다고 함
            즉 리프노드를 계속 제거하다 보면 가운데만 남아있는데 이게 루트이어야 한다고 함

            역시 단순 탐색으로 풀수 있는 문제가 아니였음 ㅋㅋㅋㅋ
            리프노드를 제거하면서 찾는다는 알고리즘??? 이 가장 중요한듯..

            어렵네 ㅋㅋ

        '''

        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        # 연결 정보가 하나 밖에 없는 노드가 리프노드
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        while n > 2:

            # 현재 리프노드의 개수 만큼 빼기
            n -= len(leaves)
            new_leaves = []

            # 리프노드와 연결된 노드에서 리프노드 연결정보 없애기
            for leaf in leaves:
                neighbor = graph[leaf].pop() # 리프노드와 연결된 노드
                graph[neighbor].remove(leaf) # 찾은 노드에서 리프노드 연결정보 없애기

                # 이러한 과정에서 새로운 리프노드가 생기면 담아두기
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            # 새로운 리프노드로 갱신
            leaves = new_leaves

        return leaves

obj = Solution()
print(obj.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))