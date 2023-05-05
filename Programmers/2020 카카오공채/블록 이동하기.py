import collections

def checkNextBoardLength(next_loc, max_length):

    left_x, left_y, right_x, right_y = next_loc

    if 0 <= left_x < max_length and 0 <= left_y < max_length:
        if 0 <= right_x < max_length and 0 <= right_y < max_length:
            return True
        
    return False

def checkBoardValue(left_value, right_value):
    if left_value == 0 and right_value == 0:
        return True
    
    return False

def checkMoveBoard(now_value, next_value):
    if now_value >= next_value:
        return True
    
    return False

def checkRotaion(now_locs, board, vector):

    left_x, left_y, right_x, right_y = now_locs
    dlx, dly, drx, dry = vector

    next_left_x = left_x + dlx
    next_left_y = left_y + dly
    next_right_x = right_x + drx
    next_right_y = right_y + dry
    next_loc = [next_left_x, next_left_y, next_right_x, next_right_y]

    if checkNextBoardLength(next_loc, len(board)) and\
        checkBoardValue(board[next_left_y][next_left_x], board[next_right_y][next_right_x]):
        return True
    
    return False

def getRotaionLocs(now_locs, board, move_board):

    left_x, left_y, right_x, right_y, now_second = now_locs
    next_second = now_second + 1

    rotation_locs = []
    arrow = 0

    # 로봇이 가로
    if left_y - right_y == 0:

        # 아래로 회전, 위로 회전 체크
        check_vectors = [[0, 1, 0, 1], [0, -1, 0, -1]]
        for vectors in check_vectors:
            if checkRotaion(now_locs[:-1], board, vectors):
                if move_board[arrow][right_y + vectors[1]][right_x] >= next_second:
                    rotation_locs.append([right_x, right_y + vectors[1], right_x, right_y, next_second])
                    move_board[arrow][right_y + vectors[1]][right_x] = next_second
                
                if move_board[arrow][left_y + vectors[1]][left_x] >= next_second:
                    rotation_locs.append([left_x, left_y, left_x, left_y + vectors[1], next_second])
                    move_board[arrow][left_y + vectors[1]][left_x] = next_second


    # 로봇이 세로
    else:

        arrow = 1

        check_vectors = [[1, 0, 1, 0], [-1, 0, -1, 0]]
        for vectors in check_vectors:
            if checkRotaion(now_locs[:-1], board, vectors):
                if move_board[arrow][right_y][right_x + vectors[0]] >= next_second:
                    rotation_locs.append([right_x + vectors[0], right_y, right_x, right_y, next_second])
                    move_board[arrow][right_y][right_x + vectors[0]] = next_second
                
                if move_board[arrow][left_y][left_x + vectors[0]] >= next_second:
                    rotation_locs.append([left_x, left_y, left_x + vectors[0], left_y, next_second])
                    move_board[arrow][left_y][left_x + vectors[0]] = next_second

    return rotation_locs

def getNextLocs(now_locs, board, move_board):

    max_length = len(board)
    vectors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    left_x, left_y, right_x, right_y, now_second = now_locs
    next_second = now_second + 1

    next_locs = []
    for dx, dy in vectors:
        next_loc = [left_x + dx, left_y + dy, right_x + dx, right_y + dy]

        if checkNextBoardLength(next_loc, max_length):
            if checkBoardValue(board[next_loc[1]][next_loc[0]], board[next_loc[3]][next_loc[2]]):

                arrow = 0

                if next_loc[1] - next_loc[3] != 0:
                    arrow = 1
                
                if checkMoveBoard(move_board[arrow][next_loc[1]][next_loc[0]], next_second) or checkMoveBoard(move_board[arrow][next_loc[3]][next_loc[2]], next_second):
                    move_board[arrow][next_loc[1]][next_loc[0]] = min(next_second, move_board[arrow][next_loc[1]][next_loc[0]])
                    move_board[arrow][next_loc[3]][next_loc[2]] = min(next_second, move_board[arrow][next_loc[3]][next_loc[2]])
                    next_loc.append(next_second)
                    next_locs.append(next_loc)
                

    return next_locs

def solution(board):

    '''
        나의 풀이(...3레벨 너무 힘든듯 ㅋㅋ 또 3시간 ㅋㅋㅋ)
        로봇을 이리저리 움직여서 
        목표지점까지 가는데 걸리는 시간을 구하는 문제

        나의 접근법
        BFS로 했고 로봇의 위치? 방향?에 따라 이동 시간을 따로 둠
        ex) 가로, 세로 인 2개의 2차원 리스트 -> 3차원 리스트

        2020 카카오 여름 인턴 문제인 경주로 건설 문제랑 유사한듯??
        그것도 방향에 따라서 4개의 2차원 리스트를 BFS 이동 보드로 사용한 풀이가 있었음
        그래도 예전에는 못풀어서 포기하고 그랬는데
        지금은 그래도 3레벨 문제 조금씩 풀고 있는듯....???????? ㅋㅋ
    '''

    queue = collections.deque()
    move_board = [[[float('inf')] * len(board) for _ in range(len(board))] for _ in range(2)]
    move_locs = []

    # 처음 시작 위치 넣어주기
    # 왼쪽 x,y , 오른쪽 x,y , 이동시간
    queue.append([0, 0, 1, 0, 0])
    move_locs = [[0, 0, 1, 0, 0]]

    # 현재는 로봇이 가로로 되어 있으니 해당 위치 초기화
    move_board[0][0][0] = -1
    move_board[0][0][1] = -1

    # BFS 시작
    while queue:

        now_locs = queue.popleft()
        
        # 로봇이 상하좌우로 움직일 수 있는 곳 가져오기
        next_locs = getNextLocs(now_locs, board, move_board)

        # 로봇이 90도로 회전할 수 있는 곳 가져오기
        for rotation_loc in getRotaionLocs(now_locs, board, move_board):
            next_locs.extend([rotation_loc])
    
        # 현재까지 이동한 곳과 겹치지 않게 queue에 넣어두기
        if next_locs:
            for next_loc in next_locs:
                if next_loc not in move_locs:
                    queue.append(next_loc)
                    move_locs.append(next_loc)
            

        print(queue)
        for l in board:
            print(l)
        print()
        for l in move_board:
            for z in l:
                print(z)
            print()
    
        print('\n\n')
            
    # 가로로 이동했을 때와 세로로 이동했을때 더 작은값이 정답
    return min(move_board[1][-1][-1], move_board[0][-1][-1])

#solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])

solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def firstSolu(board):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        엄청 깔끔하게 푸심 ㄷㄷㄷㄷ
        현재 로봇의 형태? -> 세로로 있는지 가로로 있는지를 체크
        형태를 기록하고 왼쪽 다리?를 기준으로 이동을 함

        굳이 나처럼 두 좌표를 가지고 하는 것이 아니라
        하나의 기준점과 방향을 가지고 하니 훨씬 깔끔한듯?? ㅋㅋㅋㅋ
    '''

    SIZE = len(board)
    ROW_WISE, COLUMN_WISE = range(2)
    OPEN, WALL = range(2)
    START = (0, 0, ROW_WISE)
    END_POINT = (SIZE-1, SIZE-1)
    DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    queue = collections.deque([START])
    
    # 방문 여부 체크
    visited = set()
    visited.add(START)
    moves_count = 0

    def _is_in_range(r, c):
        return 0 <= r < SIZE and 0 <= c < SIZE

    def _is_open(r, c):
        return board[r][c] == OPEN

    def _is_ok(r, c):
        return _is_in_range(r, c) and _is_open(r, c)
    
    def _yield_moves_rowwise(r, c):
        # 상하좌우 이동
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            if _is_ok(new_r, new_c) and _is_ok(new_r, new_c + 1):
                yield (new_r, new_c, ROW_WISE)
        # 회전
        if _is_ok(r+1, c) and _is_ok(r+1, c+1):
            yield (r, c, COLUMN_WISE)
            yield (r, c+1, COLUMN_WISE)
        if _is_ok(r-1, c) and _is_ok(r-1, c+1):
            yield (r-1, c, COLUMN_WISE)
            yield (r-1, c+1, COLUMN_WISE)
    
    def _yield_moves_columnwise(r, c):

        # 상하좌우 이동
        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            if _is_ok(new_r, new_c) and _is_ok(new_r+1, new_c):
                yield (new_r, new_c, COLUMN_WISE)
        
        # 회전
        if _is_ok(r, c-1) and _is_ok(r+1, c-1):
            yield (r, c-1, ROW_WISE)
            yield (r+1, c-1, ROW_WISE)
        if _is_ok(r, c+1) and _is_ok(r+1, c+1):
            yield (r, c, ROW_WISE)
            yield (r+1, c, ROW_WISE)

    while queue:
        moves_count += 1

        for _ in range(len(queue)):
            r, c, direction = queue.popleft()

            # 방향에 따른 구분
            if direction == ROW_WISE:
                yield_func = _yield_moves_rowwise
            else:
                yield_func = _yield_moves_columnwise
            
            for new_coord in yield_func(r, c):
                if new_coord not in visited:
                    queue.append(new_coord)
                    visited.add(new_coord)

                    r, c, direction = new_coord
                    if (r, c+1) == END_POINT or (r+1, c) == END_POINT:
                        return moves_count