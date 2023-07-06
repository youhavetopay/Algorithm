
'''
    백준 11403. 경로 찾기
    방향 있는 그래프에서 i -> j(i도 될 수 있음) 으로 가는 길의 길이가 
    양수인 경로가 있느지 없는지 체크하고
    이를 리스트로 나타내는 문제 

'''

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

'''
    나의 풀이

    나의 접근법
    처음에 길이가 양수 라고 했을때
    아니 그럼 음수인 길이가 있나 라고 하며 뭐지 라고 생각했는데
    생각해보니까 자기 자신에게 돌아오는 경로가 있는지도 체크하라는 내용이였음 ㅋㅋ

    방향 있는 그래프를 defaultdict으로 나타내고
    0 ~ N-1 까지 반복문을 돌면서 dfs로 찾는 방식으로 품

    문제를 풀고 보니 그냥 방향 그래프의 탐색 문제라서
    그렇게?? 어려운 문제는 아닌듯함
    그래프 문제와 그래프 탐색을 할 줄 알면 쉽게 풀 수 있을듯??
'''

def make_graph(board):

    graph = defaultdict(list)

    for i, line in enumerate(board):
        for j, connetion in enumerate(line):
            if connetion == 1:
                graph[i].append(j)
    
    return graph


N = int(input())
board = []

for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

# N = 7
# board = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 0, 0]
# ]

can_visit = [[0] * N for _ in range(N)]

graph = make_graph(board)

for i in range(N):
    visit = [False] * N
    def dfs(root, now, path_length):
        
        if path_length > 0:
            can_visit[root][now] = 1
            visit[now] = True
        for next in graph[now]:
            if visit[next] == False:
                dfs(root, next, path_length + 1)
    
        return
    
    dfs(i, i , 0)


for l in can_visit:
    for d in l:
        print(d, end=" ")
    
    print()


def firstSolu():

    '''
        다른 사람 풀이
        https://whitehairhan.tistory.com/333

        플로이드 워셜 알고리즘을 사용한 풀이
        플로이드 워셜 알고리즘은 모든 정점에서 다른 모든 정점으로 가는 최단 거리를 구하는 알고리즘

        이를 활용해서 한듯?
        근데 시간복잡도가 N^3 이라서 조금 느린듯 함
        내껀 80ms 인데 이건 180ms 정도??
    '''

    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][i] and graph[i][k]:
                    graph[j][k] = 1
                    
    for g in graph:
        print(*g)