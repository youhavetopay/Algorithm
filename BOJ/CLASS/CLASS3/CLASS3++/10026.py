
'''
    백준 10026. 적록색약

    R,G,B 로 이루어진 문자열 배열이 주어질때
    색약이 있는 사람과 없는 사람이 보는 구역의 개수를 구하는 문제
    그냥 BFS 하는 문제 ㅋㅋ 
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

painting = []
for _ in range(N):
    painting.append(list(input().rstrip()))

def solution():

    '''
        나의 풀이

        나의 접근법
        색약이 있는 사람이 보는 그림은 은 R, G를 같은 영역으로 보고 해야하고
        색약이 없는 사람이 보는 그름은 그냥 R, G, B 모두 다른 영역으로 보고
        BFS를 해주면 끝

        BFS 기본 탐색 문제에서 살~~~~~짝 변형한 느낌??

        그냥 나는 BFS 두번 했음 ㅋㅋ
    '''

    global N, painting

    visited = [[False] * N for _ in range(N)]

    def bfs(x, y, color_weakness):
        
        # 색약이 있고 지금 탐색하는 영역이 'R' 혹은 'G' 인 경우
        # 같은 영역으로 보기
        now_color = [painting[y][x]]
        if color_weakness and painting[y][x] in ['R', 'G']:
            now_color = ['R', 'G']

        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue.append([x, y])
        visited[y][x] = True

        while queue:

            now_x, now_y = queue.popleft()

            for dx, dy in directions:
                next_x, next_y = now_x + dx, now_y + dy
                if (0 <= next_x < N and 0 <= next_y < N) \
                    and visited[next_y][next_x] == False \
                    and painting[next_y][next_x] in now_color:

                    visited[next_y][next_x] = True
                    queue.append([next_x, next_y])

        return

    # 색약이 없는 사람의 영역 개수 찾기
    grid = 0
    for y in range(N):
        for x in range(N):
            if visited[y][x] == False:
                bfs(x, y, False)
                grid += 1

    # 색약이 있는 사람의 영역 개수 찾기
    color_weakness_grid = 0
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x] == False:
                bfs(x, y, True)
                color_weakness_grid += 1

    print(grid, color_weakness_grid)

solution()

def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@uoayop/BOJ-10026-%EC%A0%81%EB%A1%9D%EC%83%89%EC%95%BD-Python

        DFS로 하심
        그 외에는 나랑 똑같이 탐색 두번 했는데
        색약이 있는 사람을 기준으로 탐색을 할때는
        입력했던 그림의 R 인 곳을 G 로 전부 바꾸고 나서
        탐색을 하심

        나머지는 나랑 똑같음
    '''

    sys.setrecursionlimit(100_000)

    n = int(input().rstrip())
    matrix = [list(input().rstrip()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    three_cnt, two_cnt = 0, 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):

        visited[x][y] = True
        current_color = matrix[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < n) and (0 <= ny < n):
                if visited[nx][ny] == False:
                    if matrix[nx][ny] == current_color:
                        dfs(nx, ny)
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                dfs(i, j)
                three_cnt += 1
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'R':
                matrix[i][j] = 'G'
    
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                dfs(i, j)
                two_cnt += 1

    print(three_cnt, two_cnt)
