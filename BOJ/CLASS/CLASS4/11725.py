
'''
    백준 11725. 트리의 부모 찾기

    트리 연결 정보가 주어지면 노드의 부모가 누구인지 출력하는 문제
'''

import sys
from collections import defaultdict
sys.setrecursionlimit(200_000)
input = sys.stdin.readline

N = int(input())
road = [list(map(int, input().split())) for _ in range(N-1)]

# N = 7
# road = [
#     [1, 6],
#     [6, 3],
#     [3, 5],
#     [4, 1],
#     [2, 4],
#     [4, 7]
# ]


# N = 12
# road = [
#     [1, 2],
#     [1, 3],
#     [2, 4],
#     [3, 5],
#     [3, 6],
#     [4, 7],
#     [4, 8],
#     [5, 9],
#     [5, 10],
#     [6, 11],
#     [6, 12]
# ]

# N = 5
# road = [

# [1, 4],
# [4, 5],
# [5, 3],
# [3, 2]
# ]

def solution(n, load):

    '''
        나의 풀이

        나의 접근법
        처음엔 그냥 연결 정보를 바탕으로 DFS를 했는데
        시간초과 뜸 ㅋㅋㅋ
        데이터 제한이 10만이라서 
        노드를 방문할때마다 계속 연결정보를 전부 탐색하기 때문에 그런것 같았음 

        그래서 생각한게 
        트리를 그래프 처럼 나타내고
        1부터 DFS를 시작하면 될 것같아서 해보니 통과 ㅋㅋ
    '''

    # 트리 만들기
    # 트리가 그래프는 아니지만 ㅋㅋ 
    # 그냥 습관적으로 graph 라고 함 ㅋㅋㅋ
    graph = defaultdict(list)

    for a, b in load:
        graph[a].append(b)
        graph[b].append(a)

    # 부모 정보
    parents = {1:-1}

    # 방문 여부
    visited = [False] * (n + 1)

    visited[1] = True

    def dfs(now):

        # 아직 방문하지 않은 노드 -> 자식 노드
        for next in graph[now]:
            if visited[next] == False:
                parents[next] = now
                visited[next] = True
                dfs(next)

    dfs(1)

    for i in range(2, n+1):
        print(parents[i])


    return

solution(N, road)

from collections import deque
def firstSolu():

    '''
        다른 사람 풀이
        https://d-cron.tistory.com/22

        나랑 똑같이 DFS로 한 풀이도 있고
        BFS로 한 방법도 있어서
        BFS 한 코드를 가져옴 

        그래프를 2차원 배열로 나타냈는데
        연결된 index만 넣어줌으로 시간복잡도를 줄였다고 함
        
        나는 처음에 초기화 해주는게 귀찮아서 defaultdict을 주로 사용하는데
        이렇게 2차원 배열로 나타내는 방법도 디게 좋은 방법인 것 같음
    '''

    N = int(sys.stdin.readline())
    graph = [[] for i in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append(1)

    ans = [0]*(N+1)

    def bfs():
        while queue:
            now = queue.popleft()
            for nxt in graph[now]:
                if ans[nxt] == 0:
                    ans[nxt] = now
                    queue.append(nxt)

    bfs()
    res = ans[2:]
    for x in res:
        print(x)