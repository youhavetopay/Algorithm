
'''
    백준 16236. 아기 상어
    
    아기 상어가 먹을 수 있는 물고기를 
    모두 먹는데 걸리는 시간을 계산하는 문제
'''

import sys
from collections import deque

input = sys.stdin.readline

def find_fish_loc(board, shark_loc, shark_size):

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    board_size = len(board)

    queue = deque()
    visited = set()
    queue.append([shark_loc[0], shark_loc[1]])
    visited.add((shark_loc[0], shark_loc[1]))

    dist = 0

    fishs = set()

    while queue:

        nexts = []

        while queue:
            now_x, now_y = queue.popleft()

            for dx, dy in directions:
                nx, ny = now_x + dx, now_y + dy

                if 0 <= nx < board_size and 0 <= ny < board_size and (nx, ny) not in visited:
                    visited.add((nx, ny))

                    if board[ny][nx] != 0:
                        if board[ny][nx] < shark_size:
                            fishs.add((nx, ny))
                        elif board[ny][nx] > shark_size:
                            continue
                        else:
                            nexts.append([nx, ny])
                    else:
                        nexts.append([nx, ny])
        
        dist += 1

        if len(fishs) == 0:
            queue.extend(nexts)

    fishs = sorted(list(fishs), key=lambda x: (x[1], x[0]))
    

    if len(fishs) == 0:
        return [[-1, -1], 0]

    else:
        return [fishs[0], dist]
            




def solution():

    '''
        나의 풀이
        매 턴? 마다 BFS를 하면서 먹을 수 있는 가장 가까운 물고기를 찾고
        먹고 반복하는 방식으로 품

        문제 설명이 좀 길어서 그렇지 그냥 BFS 잘하면 되는 듯ㅋㅋㅋ

        근데 문제 설명에서 아기 상어 좀 귀여운듯 ㅋㅋㅋㅋㅋ
        엄마 상어한테 도와달라고 한데 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    answer = 0

    N = int(input())

    board = []

    shark_loc = [-1, -1]
    shark_size = 2
    eat_count = 0

    for _ in range(N):
        board.append(list(map(int, input().split())))

        if shark_loc[0] == -1:
            for i in range(N):
                if board[-1][i] == 9:
                    shark_loc = [i, len(board) - 1]


    # N = 4

    # board = []

    # temp = [
    #     [4, 3, 2, 1],
    #     [0, 0, 0, 0],
    #     [0, 0, 9, 0],
    #     [1, 2, 3, 4]
    # ]

    # shark_loc = [-1, -1]
    # shark_size = 2
    # eat_count = 0

    # for _ in range(N):
    #     board.append(temp[_])

    #     if shark_loc[0] == -1:
    #         for i in range(N):
    #             if board[-1][i] == 9:
    #                 shark_loc = [i, len(board) - 1]

    board[shark_loc[1]][shark_loc[0]] = 0

    while True:
        
        fish_loc, moved = find_fish_loc(board, shark_loc, shark_size)

        if fish_loc[0] == -1:
            break
        
        board[fish_loc[1]][fish_loc[0]] = 0

        eat_count += 1
        if shark_size == eat_count:
            shark_size += 1
            eat_count = 0

        shark_loc = fish_loc
        answer += moved

    print(answer)
    


solution()



def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@waoderboy/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-16236-%EC%95%84%EA%B8%B0%EC%83%81%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

        전체적으로 나랑 비슷한 접근과 비슷한 풀이법 ㅋㅋ
    '''
    
    N = int(input)
    space = [list(map(int, input().split())) for _ in range(N)]

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    pos = []
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                pos.append(i)
                pos.append(j)
    
    cnt = 0

    def bfs(x, y):
        nonlocal N
        
        visited = [[0] * N for _ in range(N)]
        queue = deque([x, y])
        cand = []

        visited[x][y] = 1

        while queue:
            i, j = queue.popleft()

            for idx in range(4):
                ii, jj = i + dx[idx], j + dy[idx]

                if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
                    if space[x][y] > space[ii][jj] and space[ii][jj] != 0:
                        visited[ii][jj] = visited[i][j] + 1
                        cand.append((visited[ii][jj] - 1, ii, jj))
                    elif space[x][y] == space[ii][jj]:
                        visited[ii][jj] = visited[i][j] + 1
                        queue.append([ii, jj])
                    elif space[ii][jj] == 0:
                        visited[ii][jj] = visited[i][j] + 1
                        queue.append([ii, jj])
            
        return sorted(cand, key = lambda x: (x[0], x[1], x[2]))
    
    i, j = pos
    size = [2, 0]

    while True:
        space[i][j] = size[0]
        cand = deque(bfs(i, j))

        if not cand:
            break

        step, xx, yy = cand.popleft()
        cnt += step
        size[1] += 1

        if size[0] == size[1]:
            size[0] += 1
            size[1] = 0
        
        space[i][j] = 0
        i, j = xx, yy
    
    print(cnt)