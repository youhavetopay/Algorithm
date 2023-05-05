import collections
from typing import List

def checkLength(m, n, j, i):
    if i < m and j < n:
        return True
    
    return False

def BFS(board, j, i):
    vectors = [[1, 0], [0, 1]]

    queue = collections.deque([[j, i]])
    check_board = collections.defaultdict(list)
    check_board[i].append([j, i])

    block = board[i][j]

    # BFS
    while queue:
        x, y = queue.popleft()

        for vec in vectors:
            now_x, now_y = x + vec[0], y + vec[1] 
            
            # 길이를 초과하지 않고
            # 처음 시작한 블록과 같은 블록이며
            # 방문을 하지 않는 블록을 queue에 추가
            if checkLength(len(board), len(board[0]), now_x, now_y) \
                and board[now_y][now_x] == block \
                and [now_x, now_y] not in check_board[now_y]:

                queue.append([now_x, now_y])
                check_board[now_y].append([now_x, now_y])

    print(block, check_board)


    # 2 x 2 인지 체크하는 로직
    # 이 부분을 완성하지 못함 ㅠㅠㅠ
    if len(check_board.keys()) < 2:
        return []
    
    return_list = []
    for values in check_board.values():
        if len(values) < 2:
            return []
        
        for value in values:
            return_list.append(value)

    return return_list

def solution(m, n, board):


    '''
        나의 풀이(못품 ㅋㅋㅋㅋ)

        대충 애니팡 비스무리한 게임을 만드는 문제

        엄청난 똥꼬쇼를 했지만 못품 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    answer = 0

    board = [
        list(line) for line in board
    ]

    vectors = [[1, 0], [0, 1]]

    for temp in board:
        print(temp)
    print()
    
    
    while True:

        # 삭제할 블록 위치
        delete_list = set()

        # 전체를 반복
        for i in range(m):
            for j in range(n):
                block = board[i][j]
                
                # 만약 삭제할 리스트에 있거나 이미 삭제한 경우
                if str(i) + str(j) in delete_list or block == '':
                    continue
                
                # BFS를 시작할 조건
                # 오른쪽이랑 아래쪽에 나랑 같은 블록이 있어야 BFS 시작
                for vec in vectors:
                    now_x, now_y = j + vec[0], i + vec[1]

                    if checkLength(m, n, now_x, now_y) \
                        and board[now_y][now_x] != block:
                        break
                    elif now_x >= n or now_y >= m:
                        break
                else:

                    # BFS해서 가져온 삭제할 블록 추가
                    for loc in BFS(board, j, i):
                        str_loc = str(loc[0]) + str(loc[1])
                        delete_list.add(str_loc)
                    
                    print(delete_list)
                    print()
                    
                            
        if len(delete_list) == 0:
            break
        
        # 삭제 개수 더해주고 블록 삭제해주기
        answer += len(delete_list)
        for loc in delete_list:
            x, y = int(loc[0]), int(loc[1])
            board[y][x] = ''

        for temp in board:
            print(temp)
        print()

        # 밑에서 부터 위에 떠있는 블록 있으면 내려주기
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                last_y = i
                next_y = i + 1
                while checkLength(m, n, j, next_y) \
                    and (board[last_y][j] != '' and board[next_y][j] == ''):
                         board[last_y][j], board[next_y][j] = board[next_y][j], board[last_y][j]
                         last_y = next_y
                         next_y += 1
        
        for temp in board:
            print(temp)
        print()
        print(answer)

        break
        

    return answer

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))


def firstSoul(m: int, n: int, board: List[str]) -> int:

    '''
        책 풀이
        와우 ㅋㅋㅋㅋㅋㅋ

        문제 자체가 구현 문제라서 조금 복잡하다고 함

        1. 삭제할 수 있는 블록 찾기
        2. 블록 삭제
        3. 블록 아래로 내리기

        이렇게 3가지를 구현해야해서 조금 복잡했다고 함

        근데 난 너무 또 어렵게 푼듯 ㅋㅋㅋㅋㅋ
    '''

    board = [list(x) for x in board]

    matched = True
    while matched:

        matched = []

        # 리스트를 순회하면서
        # 나를 기준으로 아래, 오른쪽, 오른쪽아래 대각선 이 빈칸이 아니고 전부 같다면
        # 삭제할 리스트에 넣어주기
        for i in range(m-1): # 이렇게 하면 길이 유효성 체크 안해도 될듯..
            for j in range(n-1):
                if board[i][j] == \
                    board[i][j + 1] == \
                    board[i + 1][j+1] == \
                    board[i+1][j] != '#':
                    matched.append([i, j])
        
        # 전부 삭제하기
        for i, j in matched:
            board[i][j] = board[i][j+1] = board[i+1][j+1] = board[i+1][j] = '#'
        
        # 아래로 내리기
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'

    # 삭제한 블록 개수 반환
    return sum(x.count('#') for x in board)
