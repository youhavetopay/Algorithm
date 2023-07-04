
'''
    백준 14940 쉬운 최단거리
    
    나의 풀이
    입력이 주어지면 목적지까지의 최단거리를
    각자의 위치에서 기록한 후 반환하고
    만약 못 가는 경우에는 아예 못 가는 곳은 0
    가로막혀 있어서 못가는 경우는 -1로 하는 문제

    나의 접근법
    그냥 목적지에서 출발하고 출발지에 도착하는 최단거리를
    구하는 방식으로 함 -> BFS
    queue를 다 비울 때까지 반복 한 후
    다시 순회를 돌면서 방문하지 않았던 1인 곳을 -1로 바꿔줌

    문제를 잘 제대로 않 읽고 -1하는 과정을 하지 않아서
    왜 자꾸 틀리지?? 이 생각함 ㅋㅋㅋㅋ
    문제 잘 읽자..

'''


import sys
from collections import deque
input = sys.stdin.readline

def mySolu():
    n, m = map(int, input().split())

    input_board = ['2 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 0 0 0 0 1',
    '1 1 1 1 1 1 1 1 1 1 0 1 1 1 1',
    '1 1 1 1 1 1 1 1 1 1 0 1 0 0 0',
    '1 1 1 1 1 1 1 1 1 1 0 1 1 1 1']

    board = []
    x, y = -1, -1
    for i, input_board_line in enumerate(input_board):
        line = list(map(int, input_board_line.split()))
        if 2 in line:
            x, y = line.index(2), i
        board.append(line)



    # n, m = 15, 15

    # x, y = 0, 0

    vectors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque()
    queue.append([x, y, 0])
    visited = set()
    visited.add((x, y))

    while queue:

        now_x, now_y, moved = queue.popleft()
        board[now_y][now_x] = moved

        for dx, dy in vectors:
            next_x, next_y = now_x + dx, now_y + dy
            if 0 <= next_x < m and 0 <= next_y < n:
                if (next_x, next_y) not in visited and board[next_y][next_x] != 0:
                    queue.append([next_x, next_y, moved+1])
                    visited.add((next_x, next_y))

    for y in range(n):
        for x in range(m):
            if (x, y) not in visited and board[y][x] == 1:
                board[y][x] = -1


    for line in board:

        for i, num in enumerate(line):
            if i == m-1:
                print(num)
            else:
                print(num, end = ' ')





def firstSolu():

    '''
        다른 사람 풀이
        https://star7sss.tistory.com/370

        나랑 똑같이 BFS로 했지만
        방문 여부를 체크하는 방식과
        못가는 영역의 체크하는 부분이 다름

        방문 여부체크를 나는 set으로 했고 이 분은 리스트로 체크하심
        또한 못가는 영역을 미리 -1로 초기화하고
        벽(0 인 부분) 을 미리 체크해서 좀 더 빠를 듯??
    '''

    N, M = map(int, input().split())
    board = []
    queue = deque([])
    visit = [[False] * M for _ in range(N)]
    res = [[-1] * M for _ in range(N)]

    for i in range(N):
        row = list(map(int, input().split()))

        for j in range(M):
            if row[j] == 2:
                queue.append((i, j))
                visit[i][j] = True
                res[i][j] = 0
            
            if row[j] == 0:
                res[i][j] = 0
        
        board.append(row)

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny] == 1:
                queue.append((nx, ny))
                visit[nx][ny] = True
                res[nx][ny] = res[x][y] + 1
    
    for row in res:
        for i in row:
            print(i, end=" ")
        
        print()