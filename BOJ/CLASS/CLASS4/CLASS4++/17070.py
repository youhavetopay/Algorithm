
'''
    백준 17070. 파이프 옮기기 1
    일정 방향으로 규칙에 따라 파이프를 설치할 때
    N, N 으로 이어지는 파이프를 설치하는 경우의 수를 계산하는 문제

'''

import sys
input = sys.stdin.readline

def solution():

    '''
        나의 풀이

        나의 접근법
        DFS로 모든 경우의 수를 계산해도 괜찮을것 같아서
        (정답이 1백만개 이하라고 했음)

        해봤더니 시간초과가 떴음...

        그래서 문제 유형을 봤는데 다이나믹 프로그래밍이라고 되어 있어서 
        멘붕 ㅋㅋㅋㅋㅋㅋㅋ

        그래서 질문하기 게시판을 봤는데

        그냥 N, N 지점에 1이면 탐색 안하도록 넣으면 된다고 해서
        해봤더니 통과함 ㅋㅋㅋㅋㅋㅋ

        지금 보니까 쫌 무식하게 푼듯.. ㅋㅋㅋㅋ
    '''

    N = int(input())

    board = [
        list(map(int, input().split())) for _ in range(N)
    ]

    # N = 16
    

    # board = [
    #     [0] * N for _ in range(N)
    # ]

    # 파이프 초기 위치 넣어주기
    board[0][0] = 2
    board[0][1] = 2

    if board[-1][-1] == 1:
        print(0)
        return

    answer = 0

    def dfs(board, now_end, arrow):
        nonlocal answer, N

        print(now_end, arrow)

        for row in board:
            print(row)
        print()

        now_x, now_y = now_end

        max_length = N-1

        if now_x == max_length and now_y == max_length:
            answer += 1
            return
        
        if arrow == 1: # 가로

            if now_x < max_length:

                if board[now_y][now_x+1] == 0:
                    board[now_y][now_x+1] = 2
                    dfs(board, [now_x+1, now_y], 1)
                    board[now_y][now_x+1] = 0

                if now_y < max_length:
                    if board[now_y][now_x+1] == 0 and board[now_y+1][now_x] == 0 and board[now_y+1][now_x+1] == 0:
                        board[now_y][now_x+1] = 2
                        board[now_y+1][now_x] = 2
                        board[now_y+1][now_x+1] = 2

                        dfs(board, [now_x + 1, now_y + 1], 3)

                        board[now_y][now_x+1] = 0
                        board[now_y+1][now_x] = 0
                        board[now_y+1][now_x+1] = 0
                


        elif arrow == 2: # 세로

            if now_y < max_length:
                if board[now_y+1][now_x] == 0:
                    board[now_y+1][now_x] = 2
                    dfs(board, [now_x, now_y + 1], 2)
                    board[now_y+1][now_x] = 0
                
                if now_x < max_length:
                    if board[now_y][now_x+1] == 0 and board[now_y+1][now_x] == 0 and board[now_y+1][now_x+1] == 0:
                        board[now_y][now_x+1] = 2
                        board[now_y+1][now_x] = 2
                        board[now_y+1][now_x+1] = 2

                        dfs(board, [now_x + 1, now_y + 1], 3)

                        board[now_y][now_x+1] = 0
                        board[now_y+1][now_x] = 0
                        board[now_y+1][now_x+1] = 0


        elif arrow == 3: # 대각선

            if now_x < max_length:
                if board[now_y][now_x+1] == 0:
                    board[now_y][now_x+1] = 2
                    dfs(board, [now_x+1, now_y], 1)
                    board[now_y][now_x+1] = 0
                
            if now_y < max_length:
                if board[now_y+1][now_x] == 0:
                    board[now_y+1][now_x] = 2
                    dfs(board, [now_x, now_y + 1], 2)
                    board[now_y+1][now_x] = 0

            if now_x < max_length and now_y < max_length:
                if board[now_y][now_x+1] == 0 and board[now_y+1][now_x] == 0 and board[now_y+1][now_x+1] == 0:
                        board[now_y][now_x+1] = 2
                        board[now_y+1][now_x] = 2
                        board[now_y+1][now_x+1] = 2

                        dfs(board, [now_x + 1, now_y + 1], 3)

                        board[now_y][now_x+1] = 0
                        board[now_y+1][now_x] = 0
                        board[now_y+1][now_x+1] = 0
    
    dfs(board, [1, 0], 1)

    print(answer)

    return

solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://backtony.github.io/algorithm/2021-03-02-algorithm-boj-class4-44/

        DP 풀이

        파이프 방향에 따른 3차원 배열을 생성해두고
        초기화 해둔 다음
        
        현재 위치로 파이프를 설치할 수 있으면
        이어지는 이전 파이프 방향에 따라 더해줌??

        2차원 배열 이상을 사용하는 DP 문제는 너무 어려운듯....
    '''

    n = int(input())

    graph = [[] for _ in range(n)]

    dp = [[[0] * n for _ in range(n)] for _ in range(3)]

    for i in range(n):
        graph[i] = list(map(int, input().split()))

    # 시작 위치 초기화
    dp[0][0][1] = 1

    for i in range(2, n):
        if graph[0][i] == 0:
            dp[0][0][1] = dp[0][0][i-1]
    
    for r in range(1, n):
        for c in range(1, n):

            # 대각선
            if graph[r][c] == 0 and graph[r][c-1] == 0 and graph[r-1][c] == 0:
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            
            if graph[r][c] == 0:

                # 가로
                dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]

                # 세로
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
            
    
    print(sum(dp[i][n-1][n-1] for i in range(3)))