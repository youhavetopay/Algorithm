
'''
    백준 14502. 연구소
    벽을 최대 3개 새롭게 세울 수 있을때
    바이러스가 퍼지지 않는 안전구역의 최대 갯수를 구하는 문제
'''

import sys
input = sys.stdin.readline

from collections import deque

def bfs(board, wall, virus):

    max_x, max_y = len(board[0]), len(board)

    visited = [[0] * max_x for _ in range(max_y)]
    
    # visited 에 벽이랑 바이러스 정보 넣어주기
    for x, y in wall:
        visited[y][x] = 1

    queue = deque()

    for x, y in virus:
        queue.append([x, y])
        visited[y][x] = 1
    
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:

        now_x, now_y = queue.popleft()
        for dx, dy in direction:
            nx, ny = now_x + dx, now_y + dy
            if 0 <= nx < max_x and 0 <= ny < max_y \
                and visited[ny][nx] == 0 \
                    and board[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append([nx, ny])
    
    # 안전구역은 바이러스 방문 구역과 벽을 제외한 나머지 구역
    safe_zone = 0
    for row in visited:
        safe_zone += row.count(0)
    
    return safe_zone

    


def solution():

    '''
        나의 풀이

        나의 접근법

        다행히 N, M 크기가 최대 8이라서 완전탐색으로 풀어도 될 것 같았음
        벽을 세우는 것은 DFS 로 하고 해당 상황에서 바이러스가 퍼져서 안전구역을 
        계산하는 것은 BFS로 해서 쉽게 풀었음 ㅎㅎ

        데이터 제한이 컸다면 머리 아팠을듯 ㅋㅋㅋ
    '''

    N, M = map(int, input().split())

    board = []

    # 바이러스 위치와 벽의 위치를 저장해둠
    virus = []
    wall = []
    for y in range(N):
        row = list(map(int, input().split()))
        board.append(row)

        for x, zone in enumerate(row):
            if zone == 2:
                virus.append([x, y])
            elif zone == 1:
                wall.append([x, y])

    # 최대 안전구역
    max_safe_zone = 0

    def dfs(board, new_wall_count, y):

        nonlocal max_safe_zone

        # 새로운 벽을 3개 세웠을 때
        if new_wall_count == 3:
            
            # 현재 상태에서 안전구역 계산하기
            safe_zone = bfs(board, wall, virus)
            # for row in board:
            #     print(row)
            # print(safe_zone)
            # print()

            max_safe_zone = max(max_safe_zone, safe_zone)
            return
        
        # board 를 순회하면서 0 인 곳에 벽 세우기
        for ny in range(y, len(board)):
            for nx in range(len(board[0])):
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    wall.append([nx, ny])
                    dfs(board, new_wall_count + 1, ny)
                    wall.pop()
                    board[ny][nx] = 0
        
        return
    
    dfs(board, 0, 0)

    print(max_safe_zone)

    return

# solution()


import copy

def firstSolu():

    '''
        다른 사람 풀이
        https://jie0025.tistory.com/209

        나랑 똑같은 접근법으로 풀어내심

        근데 BFS를 할때 초기 바이러스를 계속 찾아서 넣어주는 것 때문에
        조금 오래 걸리는듯??

        이 외에는 나랑 똑같음 ㅎㅎㅎ
    '''

    d = [[-1,0],[1,0],[0,-1],[0,1]]

    n, m = map(int,input().split())
    lab_map = [list(map(int,input().split())) for _ in range(n)]

    result = 0

    def bfs():

        nonlocal result

        queue = deque()
        #queue에 2의 위치 전부 append
        test_map = copy.deepcopy(lab_map)
        for i in range(n):
            for k in range(m):
                if test_map[i][k] == 2:
                    queue.append((i,k))

        while queue:
            r,c = queue.popleft()

            for i in range(4):
                dr = r+d[i][0]
                dc = c+d[i][1]

                if (0<=dr<n) and (0<=dc<m):
                    if test_map[dr][dc] == 0:
                        test_map[dr][dc] =2
                        queue.append((dr,dc))
        count = 0
        for i in range(n):
            for k in range(m):
                if test_map[i][k] == 0:
                    count +=1

        result = max(result, count)
    
    def make_wall(count):
        if count == 3:
            bfs()
            return
        for i in range(n):
            for k in range(m):
                if lab_map[i][k] == 0:
                    lab_map[i][k] = 1
                    make_wall(count+1)
                    lab_map[i][k] = 0

    make_wall(0)

    print(result)

    
firstSolu()