from collections import defaultdict
from itertools import permutations


def calMoveDist(board, now, target):
    x, y = now
    card_x, card_y = target

    x_length = abs(card_x - x)
    y_length = abs(card_y - y)

    if x_length == 0 and y_length == 0:
        return 0

    if x_length > 0 and y_length > 0:
        move_x = 0
        if x < card_x:
            
            for dx in range(x+1, card_x + 1):
                if board[y][dx] == 0:
                    move_x += 1
                    
                else:
                    move_x = x_length
                    break
        else:
            for dx in range(x-1, card_x-1, -1):
                if board[y][dx] == 0:
                    move_x += 1
                    
                else:
                    move_x = x_length
                    break
            
        if (card_x == 0 or card_x == 3):
            move_x = 1

        move_y = 0
        if y < card_y:
            for dy in range(y+1, card_y + 1):
                if board[dy][x] == 0:
                    move_y += 1
                    
                else:
                    move_y = y_length
                    break
        else:
            for dy in range(y-1, card_y-1, -1):
                if board[dy][x] == 0:
                    move_y += 1
                    
                else:
                    move_y = y_length
                    break
            
        if (card_y == 0 or card_y == 3):
            move_y = 1

        if move_x <= move_y:
            return move_x + 1
        else:
            return move_y + 1
    
    return 1


    

def getCardKind(board):

    kind = defaultdict(list)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] != 0:
                kind[board[y][x]].append([x, y])
    
    return kind

def getNewBoard(board):
    temp_board = []

    for line in board:
        temp = []
        for x in line:
            temp.append(x)
        temp_board.append(temp)

    return temp_board

def getMoveCount(board, orders, card_order, card_info, cursor):
    
    min_move_count = float('inf')

    for order in orders:
        now_move_count = 0
        now_cursor = cursor[:]

        new_board = getNewBoard(board)
        card_order_idx = 0

        for now_card in order:
            first_card_loc = card_info[now_card][card_order[card_order_idx][0]]
            move_count = calMoveDist(new_board, now_cursor, first_card_loc)
            now_move_count += move_count
            now_move_count += 1
            now_cursor = [first_card_loc[0], first_card_loc[1]]

            new_board[first_card_loc[1]][first_card_loc[0]] = 0

            for l in new_board:
                print(l)
            print(now_move_count)
            print()

            second_card_loc = card_info[now_card][card_order[card_order_idx][1]]
            move_count = calMoveDist(new_board, now_cursor, second_card_loc)
            now_move_count += move_count
            now_move_count += 1
            now_cursor = [second_card_loc[0], second_card_loc[1]]

            new_board[second_card_loc[1]][second_card_loc[0]] = 0

            for l in new_board:
                print(l)
            print(now_move_count)
            print('\n\n')

            card_order_idx += 1
            
        min_move_count = min(min_move_count, now_move_count)

    return min_move_count

def getCardRemoveOrder(length):

    temp = []

    def dfs(now, max_length):
        if len(now) == max_length:
            temp.append(now)
            return
        
        for i in [[1, 0], [0, 1]]:
            dfs(now + [i], max_length)
        
        return
    
    dfs([], length)

    return temp

def solution(board, r, c):

    '''
        나의 풀이(못품 ㅠㅠ)
        카드 짝 맞추는 게임인데 커서 움직임을 최소로 하는
        커서의 이동 거리를 계산하는 문제

        나의 접근법
        카드 종류 별 제거 순서랑 카드 위치별 제거 순서를 전부 순열로
        만들어서 해봤으나.. 실패...
        아마 이동거리 계산하는 부분에서 에러가 있는듯 한데
        자세한 이유는 모르겠움..ㅠㅠ
        

        거의 4시간동안 해봤지만 못풀었다는게 너무 아쉬움...ㅠㅠㅠ

    '''

    card_info = getCardKind(board)
    orders = list(map(list, permutations(card_info.keys(), len(card_info))))
    card_orders = getCardRemoveOrder(len(card_info))
    cursor = [c, r]

    answer = float('inf')

    for card_order in card_orders:
        
        move_count = getMoveCount(board, orders, card_order, card_info, cursor)
        print(card_order, move_count)
        answer = min(move_count, answer)


    return answer


print(solution(
    [
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]
    ], 
    3, 3))


from copy import deepcopy
from math import inf
from collections import deque

def get_key_count(board, cy, cx, ty, tx):
    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]

    que = deque()
    que.append((cy, cx))
    visited = [[inf for _ in range(4)] for _ in range(4)]
    visited[cy][cx] = 0

    while que:
        y, x = que.popleft()
        if y == ty and x == tx:
            return visited[y][x]
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                que.append((ny, nx))
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            while 0 <= ny + dy[i] < 4 and 0 <= nx + dx[i] < 4 and board[ny][nx] == 0:
                ny, nx = ny + dy[i], nx + dx[i]
            if 0 <= ny < 4 and  0 <= nx < 4 and visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                que.append((ny, nx))

def get_coord_by_num(board, target):
    for i in range(4):
        for j in range(4):
            if board[i][j] == target:
                return i, j

answer = inf

def is_end(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
            
    return True

def dfs(board, r, c, ty1, tx1, cnt):
    global answer
    board = deepcopy(board)
    target_num = board[ty1][tx1]

    cnt += get_key_count(board, r, c, ty1, tx1)
    board[ty1][tx1] = 0

    ty2, tx2 = get_coord_by_num(board, target_num)
    cnt += get_key_count(board, ty1, tx1, ty2, tx2)
    board[ty2][tx2] = 0
    cnt += 2

    if is_end(board):
        answer = min(answer, cnt)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, ty2, tx2, i, j, cnt)
    

def firstSolu(board, r, c):


    '''
        다른 사람 풀이
        https://velog.io/@rltjr1092/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%EB%93%9C-%EC%A7%9D-%EB%A7%9E%EC%B6%94%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4

        DFS와 BFS를 활용한 풀이
        BFS로 거리 계산을 하는데
        최단 거리 계산하듯이 하나 넣어주고 컨트롤 + 이동키 로직도 BFS로 구현함 ㄷㄷ

        그리고 DFS로 전체를 순회하면서 검색을 하는 방법으로 품..

        내가 또 너무 어렵게 생각한듯....
    '''

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, r, c, i, j, 0)

    return answer