# from collections import deque

# def solution(board):
#     answer = 0
#     max_x, max_y = len(board[0]), len(board)

#     rectangle = []

#     for y in range(max_y):

#         if max_y - y < answer:
#             break

#         for x in range(max_x):
#             if max_x - x < answer:
#                 break
            
#             if board[y][x] == 1:
#                 find_length = get_rectangle_length(board, x, y)
#                 answer = max(answer, find_length)
                
        

#     return answer * answer

# def get_rectangle_length(board, x, y):

#     max_x, max_y = len(board[0]), len(board)

#     queue = deque([[x, y]])
#     direction = [[1, 0], [1, 1], [0, 1]]
#     length = 1

#     visited = set()
#     visited.add((x, y))

#     while queue:

#         now_queue_len = len(queue)

#         for _ in range(now_queue_len):
#             now_x, now_y = queue.popleft()
            
#             for dx, dy in direction:
#                 nx, ny = now_x + dx, now_y + dy

#                 if nx >= max_x or ny >= max_y:
#                     return length

#                 if board[ny][nx] == 0:
#                     return length
                
#                 if (nx, ny) not in visited:
#                     visited.add((nx, ny))
#                     queue.append([nx, ny])
                    
            
        
#         length += 1

#     return length

# temp = [[1] * 1000 for _ in range(1000)]
# # print(get_rectangle_length(temp, 0, 0))
# print(solution(temp))

'''

    프로그래머스 가장 큰 정사각형
    2차원 배열에서 1 로 이루어진 가장 큰 정사각형의 넓이를 구하는 문제
'''

def solution(board):

    '''
        나의 풀이(내가 푼게 맞나... ㅋㅋ)

        나의 접근법

        내가 시도했던 첫번째 방법은
        처음엔 배열 전체를 탐색하면서 1인 곳에 들어가서
        너비와 높이를 구하고 둘 중 더 작은 걸 기준으로 정사각형이 되는지 체크를 했는데 실패..

        두번째 방법은
        첫번째 방법처럼 1인 곳을 탐색을 하면서
        오른쪽, 아래, 대각선(오른쪽) 아래 이렇게 3곳으로 해서 BFS를 진행하고 했는데.. 시간초과..

        그러다가 결국 질문하기를 봤는데
        문제 유형이 DP 라는 걸 알았음 ㅋㅋㅋㅋ

        그렇게 보니 예전에 백준에서 2차원 DP를 활용하는 배낭 문제를 푼게 기억나서
        대충 해보니까
        현재 값이 1일때 왼쪽, 위, 대각선(왼쪽) 위 이렇게 3곳의 최소값의 +1 을 해주면 됨 ㅋㅋ
        이렇게 하면 정사각형의 크기가 계속 누적되서 구할 수 있음...

        DP 문제가 갑자기 웰케 많은거야....
        그리고 2차원 배열을 사용하는 DP 문제는 여전히 너~~~~무 어려움..
        문제 유형 몰랐으면 평생 못풀었을듯... ㅋㅋㅋㅋ
    '''

    answer = 0

    if len(board) < 2 or len(board[0]) < 2:
        for row in board:
            if 1 in row:
                return 1
        
        return 0

    for y in range(1, len(board)):
        for x in range(1, len(board[0])):

            if board[y][x] == 1:

                length = min(board[y-1][x-1], board[y-1][x], board[y][x-1]) + 1
                answer = max(answer, length)
                board[y][x] = length


    return answer ** 2
