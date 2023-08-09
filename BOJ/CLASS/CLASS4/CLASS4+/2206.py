
'''
    백준 2206. 벽 부수고 이동하기
    미로 길찾기를 하는데 한번은 벽을 부수고 지나갈 수 있어서
    고려해야하는 최단 거리 찾기 문제
'''

import sys
input = sys.stdin.readline

from collections import deque

def solution():

    '''
        나의 풀이

        나의 접근법
        BFS로 품

        처음엔 방문 여부를 set으로 했는데
        이렇게 하니까 무조건 벽을 부수고 가야할 때 꼭 필요한 곳에서 써야 하는데
        다른곳에서 써버려서 도착지점에 갈 수 있는데도 불구하고 가질 못했음

        그래서 방문체크를 3차원 배열로 했음
        visted[y][x] 는 (x,y) 에 방문한 경우 도달한 이동횟수와 벽을 부술 수 있는 횟수를 저장해둠
        이렇게 해서 이동횟수가 낮거나 벽을 부술 수 있는 횟수가 더 높으면 갱신하는 방식으로 했음

        골드 3인데도 불구하고 어제 풀었던 1865 웜홀 문제보다 쉬워서 좀 의야했음
        이 문제는 BFS 응용 문제라서 좀 쉬웠던 것 같음..

        그리고 질문 게시판에 반례가 참 잘되어 있는듯 ㅋㅋㅋ

    '''

    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(input()))
    
    visited = [
        [0] * M for _ in range(N)
    ]

    queue = deque()
    visited[0][0] = [1, 1]
    queue.append([0, 0, 1, 1])

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:

        now_x, now_y, moved, break_count = queue.popleft()
        
        if now_x == M - 1 and now_y == N - 1:
            print(moved)
            return

        for dx, dy in direction:
            next_x, next_y = now_x + dx, now_y + dy

            if 0 <= next_x < M and 0 <= next_y < N:
                if visited[next_y][next_x] == 0:
                    if board[next_y][next_x] == '0':
                        visited[next_y][next_x] = [moved+1, break_count]
                        queue.append((next_x, next_y, moved + 1, break_count))

                    elif board[next_y][next_x] == '1' and break_count == 1:
                        visited[next_y][next_x] = [moved+1, break_count]
                        queue.append((next_x, next_y, moved + 1, break_count-1))

                else:
                    if visited[next_y][next_x][0] > moved + 1:
                        visited[next_y][next_x] = [moved+1, break_count]
                        queue.append((next_x, next_y, moved + 1, break_count))
                    elif break_count > visited[next_y][next_x][1]:
                        visited[next_y][next_x] = [moved+1, break_count]
                        queue.append((next_x, next_y, moved + 1, break_count))
                    
    print(-1)
    return


solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://hongcoding.tistory.com/18

        나랑은 조금 다르게 하신듯 함
        3차원 배열을 선언해두고 
        visited[x][y][0] 은 벽을 안부순 경로
        visited[x][y][1] 은 벽을 부순 경로

        이렇게 두개로 구분해서 하심

        그래서 그런지 훨~~~~~씬 깔끔한듯 ㅋㅋㅋㅋㅋ
        구분하기도 편하고 if 문이 많이 없어서 디게 좋은 듯 함 ㅋㅋㅋㅋㅋ
    '''

    n, m = map(int, input().split())
    graph = []

    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    for i in range(n):
        graph.append(list(map(int, input())))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(x, y, z):

        nonlocal n, m
        
        queue = deque()
        queue.append((x, y, z))

        while queue:
            a, b, c = queue.popleft()

            if a == n - 1 and  b == m - 1:
                return visited[a][b][c]

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx, ny, c))
    
        return -1

    print(bfs(0, 0, 0))





