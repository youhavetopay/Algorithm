from typing import List

import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        '''
            나의 풀이
            방향이 있는 그래프에서 순환이 있는지 체크하는 문제

            문제를 이해하는데 시간이 좀 오래걸린듯함
            순환이 있는지 체크하는 문제인 걸 한참뒤에 께닫게 됨 ㅋㅋ
            재귀 DFS로 풀었고 힘들었음.. ㅋㅋ

            각각의 그래프의 정점 방문 여부를 체크하고
            연결된 정점끼리 방문을 했으면 True
            만약 이전에 방문한 정점이
            현재 방문한 정점과 연결되어 있다면 순환하고 있다는 것이니까 -> Flase

            set이 진짜 좋은게 in 연산을 할때 시간복잡도가 O(1)이라서 최적화 하는데
            진짜 좋은듯 ㅎㅎ
            
        '''

        if len(prerequisites) <= 1:
            return True

        graph = collections.defaultdict(list)

        for course, need in prerequisites:
            graph[course].append(need)
        
        check_couse = [False] * numCourses
        
        for i in range(numCourses):
            if i not in graph.keys():
                check_couse[i] = True

        def dfs(key, pre_keys):

            for course in graph[key]:

                if course in pre_keys:
                    return False

                if not check_couse[course]:
                    pre_keys.add(key)
                    result = dfs(course, pre_keys)
                    pre_keys.remove(key)

                    if not result:
                        return False
            
            check_couse[key] = True

            return True

        for i in range(numCourses):
            if not check_couse[i]:
                if not dfs(i, set()):
                    return False
                    

        return True
    
    def firstSoul(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        '''
            첫번째 책 풀이
            엥..? 이거 제출하니까 시간초과 뜸... 뭐지..???

            아마 그래프의 정점를 전부 탐색해서 그런가..?
            이미 방문했던 정점들을 다시 DFS를 해서 그런듯함..
            
            이와는 별개로 코드가 디게 깔끔함
            정답이 아니라서 그런지는 모르겠지만
            아무튼..
        '''

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
    
    def secondSoul(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        '''
            두번째 책 풀이
            위에 풀이를 개선한 버전의 풀이

            앞서 내가 지적했던..? ㅋㅋㅋㅋ
            이미 방문한 노드에 대해서 다시 DFS를 하지 않도록 
            visited (set)을 통해 최적화를 했음
            그렇게 하니까 통과함 ㅋㅋㅋㅋ

            내가 꽤나 성장했다는 느낌이 든다.. ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            열심히 하자!!!!
        '''

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False
            
        return True

obj = Solution()
#print(obj.canFinish(2, [[0,1]]))
#print(obj.canFinish(2, [[0,1], [1, 0]]))
print(obj.canFinish(3, [[0,1],[0,2],[1,2]]))

#print(obj.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))

#print(obj.canFinish(1, []))