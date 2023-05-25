def getNewBoard(board):

    new_board = []
    for line in board:
        new_board.append(line[:])
    
    return new_board

def check(board, x, y):

    if 0 <= x < len(board[0]) and 0 <= y < len(board) \
        and board[y][x] != 0:
        return True
    
    return False


def board_check(board):
    
    total = 0
    for line in board:
        total += line.count(1)
    
    return total
        

def solution(board, aloc, bloc):

    '''
        나의 풀이(못품 ㅠㅠ)
        두 사람이 이동을 반복하면서
        못움직이거나 상대방을 떨어뜨리면 이길때 이긴 사람은 최소로 움직이고 진 사람은 최대로 버틸때
        어느정도의 턴이 필요한지 구하는 문제...(설명하기도 어렵네 ㅋㅋ)

        나의 접근법
        일단 board 크기가 그렇게 크지 않기 때문에
        DFS로 이동하는 모든 경우의 수를 검색하고 
        a가 이기는 경우와 b가 이기는 경우의 턴 수를 저장
        근데 이렇게 하니까 a와 b가 최적의 수로 움직이는게 아니라서 
        정답을 찾아낼 수 가 없었음....

        최소최대 알고리즘?? 이랑 게임 이론을 알고 있어야 풀 수 있는듯?
        그리고 재귀는 당연히 잘해야 하고...

        이거 3 레벨 아닌듯 ㅡㅡ

    '''

    answer = -1

    a_win = []
    b_win = []

    if len(board) == 1 and len(board[0]) == 1:
        return 0

    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    board_count = board_check(board)

    def dfs(now_board, order, a_loc, b_loc, move_count):

        # a 턴
        if order:
            flag = True
            now_x, now_y = a_loc

            if now_board[now_y][now_x] == 0:
                for l in now_board:
                    print(l)
                print(a_loc, b_loc, move_count)
                print('b win \n')
                b_win.append(move_count)
                return

            for dx, dy in vectors:
                next_x, next_y = now_x + dx, now_y + dy
                if check(now_board, next_x, next_y):
                    flag = False
                    new_board = getNewBoard(now_board)
                    new_board[now_y][now_x] = 0
                    dfs(new_board, False, [next_x, next_y], b_loc, move_count + 1)
            
            if flag:
                for l in now_board:
                    print(l)
                print(a_loc, b_loc, move_count)
                print('b win \n')
                b_win.append(move_count)
                return

        # b 턴
        else:
            flag = True
            now_x, now_y = b_loc

            if now_board[now_y][now_x] == 0:
                for l in now_board:
                    print(l)
                print(a_loc, b_loc, move_count)
                print('a win \n')
                a_win.append(move_count)
                return

            for dx, dy in vectors:
                next_x, next_y = now_x + dx, now_y + dy
                if check(now_board, next_x, next_y):
                    flag = False
                    new_board = getNewBoard(now_board)
                    new_board[now_y][now_x] = 0
                    dfs(new_board, True, a_loc, [next_x, next_y], move_count + 1)
            
            if flag:
                for l in now_board:
                    print(l)
                print(a_loc, b_loc, move_count)
                print('a win \n')
                a_win.append(move_count)
                return
        
    dfs(board, True, [aloc[1], aloc[0]], [bloc[1], bloc[0]], 0)

    print(a_win, b_win)

    if board_count % 2 == 0:
        return max(b_win)
    else:
        return max(a_win)


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321

def firstSolu(board, aloc, bloc):

    '''
        다른 사람 풀이
        https://velog.io/@mrbartrns/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%82%AC%EB%9D%BC%EC%A7%80%EB%8A%94-%EB%B0%9C%ED%8C%90-python

        너무 어려움... ㅠㅠ
    '''

    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]

def in_range(board, y, x):
    if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
        return False    
    return True

def is_finished(board, y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(board, ny, nx) and board[ny][nx]:
            return False
    
    return True

def solve(board, y1, x1, y2, x2):

    # 움직일 수가 없을때 -> 내가 졌을 때
    if is_finished(board, y1, x1):
        return [False, 0]
    
    # 나의 턴인데 상대방이랑 같은 위치일때 -> 내가 이길때
    if y1 == y2 and x1 == x2:
        return [True, 1]
    
    min_turn = INF
    max_turn = 0
    can_win = False

    for i in range(4):
        ny = y1 + dy[i]
        nx = x1 + dx[i]
        if not in_range(board, ny, nx) or not board[ny][nx]:
            continue

        board[y1][x1] = 0
        # 다른 사람 턴으로 변경
        result = solve(board, y2, x2, ny, nx)
        # 원래대로?? 해주기???
        board[y2][x2] = 1

        # 내가 이길 수 있는 경우??
        if not result[0]:
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win:
            max_turn = max(max_turn, result[1])
        
    turn = min_turn if can_win else max_turn

    return [can_win, turn + 1]