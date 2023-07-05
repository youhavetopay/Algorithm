
'''
    백준 21736. 헌내기는 친구가 필요해

    나의 풀이
    입력이 주어지면 내가 만날 수 있는 사람이 총 몇명인지
    탐색하는 문제

    나의 접근법
    단순 그래프 탐색 문제라서
    BFS로 품

    지금까지 백준 문제 2개 풀었는데
    실버 2 난이도가 프로그래머스 2레벨 쉬운거 정도인듯??
    아직은 잘 모르겠지만 많이 풀어보면 좋을 듯함
    백준이 난이도 세분화를 잘해서 ㅋㅋ
    그리고 나의 티어를 올려줘서 더 좋은듯? ㅋㅋㅋ
'''

import sys
from collections import deque
input = sys.stdin.readline

def mysolu():
    N, M = map(int, input().split())

    campus = []

    start = [-1, -1]
    visited = [[False] * M for _ in range(N)]

    for y in range(N):
        line = list(input())
        
        for x in range(M):
            if line[x] == 'I':
                start = [x, y]
                visited[y][x] = True

        campus.append(line)


    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append(start)
    answer = 0

    while queue:

        now_x, now_y = queue.popleft()

        for dx, dy in vectors:
            next_x, next_y = now_x + dx, now_y + dy

            if 0 <= next_x < M and 0 <= next_y < N:
                if campus[next_y][next_x] != 'X' and visited[next_y][next_x] == False:
                    if campus[next_y][next_x] == 'P':
                        answer += 1
                    
                    visited[next_y][next_x] = True
                    queue.append([next_x, next_y])

    if answer == 0:
        print('TT')
    else:
        print(answer)


sys.setrecursionlimit(10**6)
def firstSolu():

    '''
        다른 사람 풀이
        https://yeoooo.github.io/algorithm/BOJ21736/

        이 분은 DFS로 하심
        사실상 문제가 그냥 탐색 문제라서
        BFS랑 DFS 중에서 하고 싶으거 하면 될듯? ㅋㅋ

        근데 궁금한점은 왜 다들 board 접근할때
        세로 인덱스를 x 라고 하는거지?
        아직까지 y라고 하는 사람 나밖에 못본듯 ㅋㅋㅋㅋ 
    '''

    n, m = list(map(int, input().split()))
    board = []
    target = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(n):
        col = list(input().rstrip())
        for c in range(len(col)):
            if col[c] == 'I':
                target = [i, c]
        
        board.append(col)
    
    visited = [[0] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    cnt = 0
    def dfs(x, y):
        global cnt
        if 0 <= x < n and 0 <= y < m and not visited[x][y]:
            visited[x][y] = 1

            if board[x][y] == 'P':
                cnt += 1
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if board[nx][ny] != 'X':
                        dfs(nx, ny)

    dfs(target[0], target[1])

    if not cnt:
        print('TT')
    else:
        print(cnt)