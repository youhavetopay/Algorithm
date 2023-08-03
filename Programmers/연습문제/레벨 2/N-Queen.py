
'''
    프로그래머스 N-Queen
    n x n 판에 서로 겹치지 않게 n 개의 퀸을 놓는 
    경우의 수를 계산하는 문제
'''

def solution(n):

    '''
        나의 풀이(완전히 내가 푼건 아님 ㅋㅋ)

        나의 접근법

        처음엔 2차원 배열에 위치를 기록하는 방식으로 했는데
        마지막 11번 케이스가 시간초과가 떴음..

        그래서 조금 다르게 생각해봤는데
        2차원 배열을 수정하는 것이 아닌
        stack에다가 넣고 빼는 방식으로 해보니까
        대각선인 경우를 체크하는게 너무 비효율적이였음..

        그래서 고민하다가 결국 힌트를 봤는데
        두 점의 기울기? 를 계산해서 
        x의 차이와 y의 차이가 같으면 기울기가 같은것 -> 같은 대각선위에 있음
        이러한 걸 이용해서 빠르게 하면 마지막 케이스도 6500ms 내로 끝낼 수 있음....

        솔직히 최대 몇개의 퀸을 놓은건 유명한 백트래킹 문제라서 대충은 알고 있었는데
        경우의 수를 찾는건 또 다른 문제여서 엄청 어려웠음... ㅠㅠㅠ
    '''

    answer = [0]

    def dfs(queen_locs, y):

        if y >= n:
            
            if len(queen_locs) == n:
                answer[0] += 1
                
            return
        
        if len(queen_locs) + (n - y+1) < n:
            return
        
        for next_x in range(n):
            if check(queen_locs, next_x, y):
                queen_locs.append([next_x, y])
                dfs(queen_locs, y+1)
                queen_locs.pop()

            
    dfs([], 0)
    

    return answer[0]


def check(stack, x, y):


    for q_x, q_y in stack:
        if q_x == x:
            return False
        
        if abs(x - q_x) == abs(y - q_y):
            return False
                
    return True

# def solution(n):
#     answer = [0]

#     board = [[0] * n for _ in range(n)]

    
#     def dfs(board, now_queen, y):

        
#         if y >= n:
#             if n == now_queen:
#                 answer[0] += 1
                
#             return
        
        
        
#         for next_x in range(len(board)):

#             if board[y][next_x] == 0:

#                 board[y][next_x] = 'q'
#                 tran_board(board, next_x, y, 1)

#                 dfs(board, now_queen + 1, y+1)

#                 board[y][next_x] = 0
#                 tran_board(board, next_x, y, -1)
        


#     dfs(board, 0, 0)
    

#     return answer[0]

# def tran_board(board, x, y, fill_word):

#     direction = [
#         [0, 1], [0, -1], # 아래, 위
#         [1, 0], [-1, 0], # 오른쪽, 왼쪽
#         [1, 1], [-1, -1], # 대각선 \
#         [-1, 1], [1, -1] # 대각선 /
#     ]

#     for dx, dy in direction:

#         next_x, next_y = x + dx, y + dy

#         while 0 <= next_x < len(board) and 0 <= next_y < len(board):
#             board[next_y][next_x] += fill_word
#             next_x += dx
#             next_y += dy

#     return

print(solution(10))