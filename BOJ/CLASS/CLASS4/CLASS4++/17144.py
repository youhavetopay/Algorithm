
'''
    백준 17144. 미세먼지 안녕!
    공기청정기가 작동하고 나서 남은 미세먼지 개수를 구하는 문제
'''


import sys
input = sys.stdin.readline

def rotation(board, clean_air_loc):

    top_x, top_y = clean_air_loc[0]
    bottom_x, bottom_y = clean_air_loc[1]

    board[top_y-1][top_x] = 0
    board[bottom_y+1][bottom_x] = 0

    # 위, 왼쪽 위에서 아래로
    for y in range(top_y-2, -1, -1):
        board[y+1][0] += board[y][0]
        board[y][0] = 0

    # 위, 오른쪽 끝에서 왼쪽 끝으로
    for x in range(1, len(board[0])):
        board[0][x-1] += board[0][x]
        board[0][x] = 0
    
    # 위, 오른쪽 아래서 위로
    for y in range(1, top_y + 1):
        board[y-1][-1] += board[y][-1]
        board[y][-1] = 0
    
    # 위, 왼쪽 밑에서 오른쪽 끝으로
    for x in range(len(board[0])-1, 1, -1):
        board[top_y][x] += board[top_y][x-1]
        board[top_y][x-1] = 0

    # 밑, 왼쪽 밑에서 위로
    for y in range(bottom_y+2, len(board)):
        board[y-1][0] += board[y][0]
        board[y][0] = 0

    # 밑, 오른쪽 밑에서 왼쪽끝으로
    for x in range(1, len(board[0])):
        board[-1][x-1] += board[-1][x]
        board[-1][x] = 0

    # 밑, 오른쪽 위에서 밑으로
    for y in range(len(board)-2, bottom_y-1, -1):
        board[y+1][-1] += board[y][-1]
        board[y][-1] = 0

    # 밑, 왼쪽 끝에서 오른쪽 끝으로
    for x in range(len(board[0])-1, 1, -1):
        board[bottom_y][x] += board[bottom_y][x-1]
        board[bottom_y][x-1] = 0

def solution():

    '''
        나의 풀이

        나의 접근법

        데이터 제한이 크질 않아서 먼지들의 이동을 구현하고
        공기청정기의 작동을 구현하면 될 것 같았음

        그런데 먼지들의 이동이 겹치는 부분이 있는 것 같아서
        3차원 배열로 먼지들의 정보를 구현했음
        1 번은 이전 상태 2번은 현재 상태 이런식으로

        처음엔 먼지들의 이동을 BFS로 해볼려고 했는데
        1 초 까진 괜찮았는데 그 다음 부터는 이상하게 되고
        먼지들의 이동이 중복으로 큐에 담기는것 같아서 포기하고
        그냥 이중 for 문으로 구현을 하니 아주 깔끔하게 되었음

        그리고 은근 공기청정기 작동을 구현하는데 애먹었음 ㅋㅋㅋ

        정말 깡으로 푼듯 ㅋㅋㅋㅋㅋㅋㅋ
        2시간 걸림 ㅋㅋㅋㅋㅋㅋ
    '''

    R, C, T = map(int, input().split())
    # R, C, T = 7, 8, 50

    # temp = [
    #     [0, 0, 0, 0, 0, 0, 0, 9],
    #     [0, 0, 0, 0, 3, 0, 0, 8],
    #     [-1, 0, 5, 0, 0, 0, 22, 0],
    #     [-1, 8, 0, 0, 0, 0, 0 ,0],
    #     [0, 0, 0 ,0 ,0 ,10, 43, 0],
    #     [0, 0, 5 ,0 ,15, 0, 0 ,0],
    #     [0, 0, 40, 0, 0, 0, 20, 0]
    # ]

    # 먼지들의 현재 상태
    board = [[[0] * C for _ in range(R)] for _ in range(2)]

    # 공기청정기 위치
    clean_air_loc = []

    # 입력 받기
    for row_i in range(R):
        row = list(map(int, input().split()))
        # row = temp[row_i]
        board[0][row_i] = row

        # 공기청정기 위치 기록하기
        if row[0] == -1:
            board[1][row_i][0] = -1
            clean_air_loc.append([0, row_i])
    
    now_time = 0

    direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
    next_board = 1
    last_board = 0

    while now_time < T:

        # 비어 있는 배열로 만들어주기
        for y in range(R):
            for x in range(C):
                if board[next_board][y][x] != -1:
                    board[next_board][y][x] = 0

        # 먼지 찾아서 이동시키기
        for y in range(R):
            for x in range(C):
                if board[last_board][y][x] >= 0:
                    now_dust = board[last_board][y][x]
                    count = 0

                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < C and 0 <= ny < R and board[next_board][ny][nx] != -1:
                            count += 1
                            board[next_board][ny][nx] += now_dust // 5
                    
                    board[next_board][y][x] += now_dust - ((now_dust // 5) * count)

     
        # 공기청정기 작동시키기
        rotation(board[next_board], clean_air_loc)

        now_time += 1
        last_board, next_board = next_board, last_board

    total_dust = 0
    for row in board[last_board]:
        for num in row:
            if num != -1:
                total_dust += num

    print(total_dust)

    return

solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://kyun2da.github.io/2021/04/20/brownsmog/

        나랑 먼지 이동에 대해서는 나랑 얼추 비슷한데
        공기청정기 작동 구현이 엄~~~~~청 대단한듯 함 ㅋㅋㅋ

        나랑은 다르게 아주 깔끔하게 풀어내심
        dx, dy, direct 를 통해 진행방향을 구현함 ㄷㄷㄷㄷ
    '''

    r, c, t = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(r)]

    up = -1
    down = -1

    for i in range(r):
        if arr[i][0] == -1:
            up = i
            down = i + 1
            break
    

    def spread():

        nonlocal c, r

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        tmp_arr = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if arr[i][j] != 0 and arr[i][j] != -1:
                    tmp = 0
                    for k in range(4):
                        nx = dx[k] + i
                        ny = dy[k] + j

                        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                            tmp_arr[nx][ny] += arr[i][j] // 5
                            tmp += arr[i][j] // 5
                    
                    arr[i][j] -= tmp
        
        for i in range(r):
            for j in range(c):
                arr[i][j] += tmp_arr[i][j]

    def air_up():

        nonlocal up

        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
        direct = 0
        before = 0
        x, y, = up, 1

        while True:
            nx = x + dx[direct]
            ny = y + dy[direct]

            if x == up and y == 0:
                break

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                direct += 1
                continue

            arr[x][y], before = before, arr[x][y]
            x = nx
            y = ny
    

    def air_down():

        nonlocal down

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        direct = 0
        before = 0
        x, y, = down, 1

        while True:
            nx = x + dx[direct]
            ny = y + dy[direct]

            if x == down and y == 0:
                break

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                direct += 1
                continue

            arr[x][y], before = before, arr[x][y]
            x = nx
            y = ny

    for _ in range(t):
        spread()
        air_up()
        air_down()
    
    answer = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                answer += arr[i][j]
    
    print(answer)