from typing import List

import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        '''
            나의 풀이
            방향 있는 그래프에서 모든 그래프를 방문하는 순서를
            반환하는 문제
            (한번 지나간 곳은 다시 못 지나감)
            모두 순회할 수 있는 경로가 여러개라면 방문 정점의 이름이 빠른걸로

            진짜 꾸역꾸역 품 ㅋㅋㅋ
            푸는데 엄청 오래걸림 한 2시간??

            DFS로 탐색을 했음에도 모든 경로를 이용하지 않았다면
            취소하고 다음 공항으로 이동하는 방식으로 품

            경로를 이용했다는 것을 어떻게 표현해야할지 몰라서 고민을 엄청함
            처음엔 단순히 무조건 사전순으로 방문하는줄 알고
            그렇게 했는데 모든 경로를 이용 않하는 경우도 있어서 다른 방법을 고민했어야 했었음
            그래서 처음에 그래프를 만들때 경로에 사용여부를 넣는 방식으로 해결함

            근데 시간, 공간복잡도 심각함.. 
            각각 하위 35%, 15%........

            풀고 나서 생각해보니까 그 쾨니스 어쩌구저쩌구 다리 문제랑 비슷한 문제인 듯
            
        '''


        graph = collections.defaultdict(list)

        for start, end in tickets:
            graph[start].append([end, True])
        
        for airport in graph.keys():
            graph[airport].sort()
        
        result = []
        
        def dfs(path):
            
            result_path = path

            for idx, [airport, yn] in enumerate(graph[path[-1]]):

                if yn:
                    graph[path[-1]][idx][1] = False
                    result_path = dfs(path + [airport])

                    if checkTicketUsing():
                        return result_path

                    graph[path[-1]][idx][1] = True

            return result_path
    
        def checkTicketUsing():
            for airport in graph.keys():
                for ariv, yn in graph[airport]:
                    if yn:
                        return False
            
            return True

        result = dfs(['JFK'])

                    

        return result

    def firstSoul(self, tickets: List[List[str]]) -> List[str]:

        '''
            첫번째 책 풀이
            
            DFS를 하는데 pop을 통해서 그래프에서 제거한 다음
            경로를 하나씩 담음 -> 근데 이게 마지막 방문 순서가 가장 먼저 들어가 있어서
            마지막에 뒤집어 줘야함

            이렇게 간단하다고...???
            DFS에 대한 이해가 필요할듯함..ㅠ
        '''

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))

            route.append(a)

        dfs('JFK')

        return route[::-1]

    def secondSoul(self, tickets: List[List[str]]) -> List[str]:

        '''
            두번째 책 풀이
            위에 첫번째 풀이 개선안

            첫번째 풀이는 pop(0)을 하는데
            이게 시간복잡도가 O(n)이라서 

            처음에 그래프를 만들때 뒤집어서 담으면
            pop() 으로 가능함

        '''

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())

            route.append(a)

        dfs('JFK')

        return route[::-1]

    def thirdSoul(self, tickets: List[List[str]]) -> List[str]:

        '''
            세번째 책 풀이
            재귀로 구현한 걸 반복문으로 바꾼 버전

            재귀는 코드를 봤을 때 이해하기 편하고..?
            반복문은 의식의 흐름대로 할 수 있어서 편하다고 함

            필자는 재귀를 좀더 연습하는 것을 추천한다고 함
        '''

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))

            route.append(stack.pop())


        return route[::-1]


obj = Solution()
#print(obj.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(obj.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))