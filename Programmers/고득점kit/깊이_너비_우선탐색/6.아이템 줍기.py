import collections

def check(rectangle, x, y, idx):

    for i in range(0, len(rectangle)):
        
        if i == idx:
            continue

        [x_l, y_l, x_r, y_r] = rectangle[i]

        width = x_r - x_l
        height = y_r - y_l

        x_l *= 2
        y_l *= 2

        x_r = x_l + (width * 2)
        y_r = y_l + (height * 2)

        if x_l < x < x_r and y_l < y < y_r:
            return False
    
    return True


def solution(rectangle, characterX, characterY, itemX, itemY):

    '''
        나의 풀이
        중첩된 사각형의 외각선을 따라서 목표 위치까지 가는 최단거리 구하는 문제

        사각형을 2차원 리스트에 표현시키고 외관선만 그리도록 함
        그 다음 외곽선을 따라 BFS하는 방식으로 품...

        와,, 겁나 어려웠음 ㅋㅋ
        일단 도형을 그래프로 나타내는데
        1 : 1로 하면 안되서 그래프를 두배로 확대시켜서 index단위를 0.5라고 생각해서 풀었어야 했었음 ㅋㅋ
        이거까지는 어찌저찌 했는데

        외곽선만 그리기 위해서 조건식을 잘못 설정해서 한참 헤맴 ㅋㅋ
        그리고 board의 크기를 그냥 최대값 102로 하면 되는데 굳이 이상하게 해서 시간 더 오래 잡아먹은듯 함 ㅋㅋ
    '''

    # 못가는 곳과 갈 수 있는 곳
    not_block = -1
    go_block = 0

    # board의 크기
    max_height = 102
    
    # board 및 방문 여부 체크
    board = [[not_block for _ in range(max_height)] for _ in range(max_height)]
    check_board = [[0 for _ in range(max_height)] for _ in range(max_height)]

    # 도형 그리기
    for idx, [x_l, y_l, x_r, y_r] in enumerate(rectangle):
        
        # 현재 도형의 너비와 높이
        width = x_r - x_l
        height = y_r - y_l

        # 2배 키운 도형
        x_l *= 2
        y_l *= 2

        x_r = x_l + (width * 2)
        y_r = y_l + (height * 2)

        # 외곽선 그려주기
        for x in range(x_l, x_r+1):

            # 외곽선이 다른 도형의 외곽선 안으로 들어가지 않을때만 그려주기
            if check(rectangle, x, y_l, idx):
                board[y_l][x] = go_block
            
            if check(rectangle, x, y_r, idx):
                board[y_r][x] = go_block

        for y in range(y_l, y_r+1):
            if check(rectangle, x_l, y, idx):
                board[y][x_l] = go_block
            
            if check(rectangle, x_r, y, idx):
                board[y][x_r] = go_block

    # BFS 시작
    queue = collections.deque()
    queue.append([characterX*2, characterY*2])
    check_board[characterY*2][characterX*2] = 1

    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    

    while queue:

        now_x, now_y = queue.popleft()
        now_board_val = board[now_y][now_x]

        for idx, [x, y] in enumerate(move):
            next_x, next_y = now_x + x, now_y + y
            if 0 <= next_x < max_height and 0 <= next_y < max_height:

                next_board_value = board[next_y][next_x]
                if next_board_value == 0 and check_board[next_y][next_x] == 0:

                    # 거리를 2배로 확장시켜서 한칸 이동시 1이 증가하는게 아닌 0.5 를 증가
                    board[next_y][next_x] = now_board_val + 0.5

                    check_board[next_y][next_x] = check_board[now_y][now_x] + 1
                    queue.append([next_x, next_y])


    # 목표 위치 값 반환
    return int(board[itemY*2][itemX*2])


print(solution([[2, 1, 3, 6], [4, 1, 5, 6], [1, 2, 6, 3], [1, 4, 6, 5]], 3, 2, 5, 4))



def firstSoul(rectangle, characterX, characterY, itemX, itemY):
    
    '''
        다른 사람 풀이
        https://velog.io/@rlaalswn3282/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EC%9D%B4%ED%85%9C-%EC%A4%8D%EA%B8%B0

        나랑 풀이 방법은 거의 똑같음
        
        대신 외곽선을 그리는 방법이 다름
        나는 너무 비효율적으로 한듯 .,...
        
        그리고 BFS로 이동을 할때 0.5를 더하는게 아닌 
        마지막에 나누기 2를 한다는 점이 다름 ㅋㅋㅋ (이런 방법이 있네 ㅋㅋ)
    '''

    answer = 0

    field = [[-1] * 102 for i in range(102)]

    for r in rectangle:

        # 그냥 좌표값 곱하기 2하면 두배 되는건데... ㅋㅋㅋㅋ
        # 나는 좌표값 곱하기 하면 그냥 위치만 이동되는줄 알고 착각함 ㅋㅋㅋㅋ
        # 너무 멍멍 한거 아님...?? ㅠㅜㅠ
        x1, y1, x2, y2 = map(lambda x: x*2, r)

        for i in range(x1, x2+1):
            for j in range(y1, y2 + 1):

                # 내부를 0 으로 채워주고
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0

                # 외곽선을 1로 채움 
                # 대신 다른 도형의 내부가 아닐때만
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = collections.deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)]

    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer
                    
