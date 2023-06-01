from collections import deque

def find_location(board, target):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == target:
                return [x, y]

def check_length(max_x, max_y, x, y):

    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    
    return False

def check_possible(board, end_loc):

    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for dx, dy in vectors:
        next_x, next_y = end_loc[0] + dx, end_loc[1] + dy
        if check_length(len(board[0]), len(board), next_x, next_y):
            if board[next_y][next_x] != '.':
                return True
        else:
            return True
    
    return False

def solution(board):

    '''
        나의 풀이
        리코쳇 로봇 게임을 구현해서 
        로봇이 시작지점에서 목표지점까지 이동할때 최소 이동거리를 구하는 문제

        나의 접근법
        BFS로 구현함

        문제 자체가 BFS의 응용 버전이라서 엄~~청 어렵진 않았음
        대신 조금 이동을 구현하는게 좀 귀찮다는 점??/
    '''

    max_x = len(board[0])
    max_y = len(board)

    # 시작 위치, 목표 위치 찾기
    start_loc = find_location(board, 'R')
    end_loc = find_location(board, 'G')

    # 목표지점 근처에 벽이 없으면 도착 절~~~~때 못함
    if not check_possible(board, end_loc):
        return -1

    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = deque()
    queue.append(start_loc + [0])

    # 최소 이동거리
    move_count = [[float('inf')] * len(board[0]) for _ in range(len(board))]
    move_count[start_loc[1]][start_loc[0]] = 0

    while queue:
        x, y, move = queue.popleft()

        for dx, dy in vectors:
            next_x, next_y = x + dx, y + dy
            last_x, last_y = x, y

            # 끝이거나 벽이 있을때까지 이동
            while check_length(max_x, max_y, next_x, next_y) and board[next_y][next_x] != 'D':
                last_x, last_y = next_x, next_y
                next_x += dx
                next_y += dy
            
            # 현재 이동거리 랑 같거나 더 빨리 왔을 때
            if move + 1 <= move_count[last_y][last_x]:
                move_count[last_y][last_x] = move + 1
                queue.append([last_x, last_y, move + 1])


        for l in move_count:
            print(l)
        print(queue)
        print()

    # 이동할 수 있을때
    if move_count[end_loc[1]][end_loc[0]] != float('inf'):
        return move_count[end_loc[1]][end_loc[0]]
    
    return -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))

def firstSolu(board):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/169199/solution_groups?language=python3

        나랑 풀이법이 똑같음
        대신 BFS를 구현하는 방법이 다름
        이분은 방문 여부만 체크해서 목표지점에 도달하면 바로 끝내는 방식으로 구현하심
    '''

    que = []

    # 시작 위치 찾기
    for x, row in enumerate(board):
        for y, each in enumerate(row):
            if board[x][y] == 'R':
                que.append((x, y, 0))
    
    visited = set()

    # BFS
    while que:
        x, y, length = que.pop(0)

        # 이미 방문했다면 다음껄로 넘어가기
        if (x, y) in visited:
            continue
        
        # 목표지점이라면 끝내기
        if board[x][y] == 'G':
            return length
        
        # 방문 체크
        visited.add((x, y))

        # 이동 시키기
        for diff_x, diff_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x + diff_x, now_y + diff_y
                if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                    now_x, now_y = next_x, next_y
                    continue
                que.append((now_x, now_y, length + 1))
                break
        
        return -1