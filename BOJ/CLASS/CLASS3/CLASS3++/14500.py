
'''
    백준 14500. 테트로미노

    M x N 크기의 배열이 주어지면
    테트리스에 나오는 블록 모양으로 덮었을때 얻는 최대 점수를 계산하는 문제
    (블록은 대칭, 회전 해도 됨)
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# N, M = 4, 10

# board = [
#     [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
#     [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
#     [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
#     [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
# ]

def solution(N, M, board):

    '''
        나의 풀이

        나의접근법
        딱봐도 이거 완전탐색일 것 같아서 좀 절망함 ㅋㅋ
        도형 위치 계산하는게 귀찮아서..ㅋㅋㅋ
        배열 크기도 500 이하라서 그냥 완전탐색하라고 만들었음 ㅋㅋㅋ

        그래서 완전탐색함 ㅋㅋ
        수직 직선, 수평 직선, 네모, 나머지수직, 나머지 수평 이런식으로 계산했는데

        직선이랑 네모는 그냥 배열 잘라서 계산했고

        나머지는 2x3, 3x2 크기로 배열을 나누고 
        도형 모양에 따른 인덱스에 따라 계산하는 방식으로 품

        도형 모양에 따른 인덱스 구하는게 제일 오래걸렸음 ㅋㅋㅋㅋ
    '''

    line_vertical = 0
    line_horizontal = 0
    box = 0

    # 수평 막대
    for y in range(N):
        for x in range(M-3):
            line_horizontal = max(line_horizontal, sum(board[y][x:x+4]))
    
    # 수직 막대
    for x in range(M):
        for y in range(N-3):
            line = 0
            for i in range(y, y+4):
                line += board[i][x]
            line_vertical = max(line_vertical, line)
    
    # 정사각형 
    for y in range(N-1):
        for x in range(M-1):
            check_box = 0

            for j in range(y, y+2):
                for i in range(x, x+2):
                    check_box += board[j][i]
            
            box = max(box, check_box)


    vertical_figures = get_figures_vertical()
    
    vertical_figures_score = 0

    # 2 X 3 사각형
    for y in range(N-2):
        for x in range(M-1):
            check_box = []

            for j in range(y, y+3):
                line = []
                for i in range(x, x+2):
                    line.append(board[j][i])
                check_box.append(line)
            
            for figure in vertical_figures:
                score = 0
                for fx, fy in figure:
                    score += check_box[fy][fx]
                
                vertical_figures_score = max(vertical_figures_score, score)


    horizontal_figures = get_figures_horizontal()
    horizontal_figures_score = 0
    for y in range(N-1):
        for x in range(M-2):
            check_box = []

            for j in range(y, y+2):
                line = []
                for i in range(x, x+3):
                    line.append(board[j][i])
                check_box.append(line)
            
            for figure in horizontal_figures:
                score = 0
                for fx, fy in figure:
                    score += check_box[fy][fx]
                
                horizontal_figures_score = max(horizontal_figures_score, score)
            
    return max(line_vertical, line_horizontal, box, vertical_figures_score, horizontal_figures_score)

def get_figures_vertical():

    figures = [
        # vertical S and Z
        [
            [0, 0],
            [0, 1],
            [1, 1],
            [1, 2]
        ],
        [
            [1, 0],
            [1, 1],
            [0, 1],
            [0, 2]
        ],


        # vertical J and L
        [
            [1, 0],
            [1, 1],
            [1, 2],
            [0, 2]
        ],
        [
            [1, 0],
            [1, 1],
            [1, 2],
            [0, 0]
        ],
        [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 2]
        ],
        [
            [0, 0],
            [0, 1],
            [0, 2],
            [1, 0]
        ],



        # vertical T right and left
        [
            [0, 0],
            [0, 1],
            [1, 1],
            [0, 2]
        ],
        [
            [1, 0],
            [0, 1],
            [1, 1],
            [1, 2]
        ]
    ]


    return figures

def get_figures_horizontal():

    

    figures = [

        # horizontal Z and S
        [
            [0, 0],
            [1, 0],
            [1, 1],
            [2, 1]
        ],
        [
            [1, 0],
            [2, 0],
            [0, 1],
            [1, 1]
        ],

        # horizontal J and L
        [
            [0, 0],
            [1, 0],
            [2, 0],
            [2, 1]
        ],
        [
            [0, 0],
            [1, 0],
            [2, 0],
            [0, 1]
        ],
        [
            [0, 0],
            [0, 1],
            [1, 1],
            [2, 1]
        ],
        [
            [2, 0],
            [0, 1],
            [1, 1],
            [2, 1]
        ],


        # horizontal T
        [
            [1, 0],
            [0, 1],
            [1, 1],
            [2, 1]
        ],
        [
            [1, 1],
            [0, 0],
            [1, 0],
            [2, 0]
        ],

    ]


    return figures

print(solution(N, M, board))

def firstSolu():

    '''
        다른 사람 풀이
        https://cijbest.tistory.com/87

        DFS로 아주 깔끔하게 풀어내심 ㅋㅋㅋ
        T 도형을 제외한 나머지 도형은 내 위치에서 4칸으로 갈 수 있는 모든 곳을 방문해서
        4칸 이동했으면 점수를 계산하는 방식으로 함

        T 도형은 그냥 상하좌우로 한칸씩만 체크하면 됨

        시간은 좀 오래걸리긴 하지만
        그래도 코드도 짧고 훨씬 깔끔하게 하신 것 같음 ㅎㅎ
    '''

    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    maxValue = 0

    def dfs(i, j, dsum, cnt):
        global maxValue

        if cnt == 4:
            maxValue = max(maxValue, dsum)
            return
        
        for n in range(4):
            ni = i + move[n][0]
            nj = j + move[n][1]

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(ni, nj, dsum + board[ni][nj], cnt + 1)
                visited[ni][nj] = False
    
    def exce(i, j):
        global maxValue

        for n in range(4):
            tmp = board[i][j]

            for k in range(3):
                t = (n + k) % 4
                ni = i + move[t][0]
                nj = j + move[t][1]

                if not (0 <= ni < N and 0 <= nj < M):
                    tmp = 0
                    break
                    
                tmp += board[ni][nj]
            
            maxValue = max(maxValue, tmp)
    
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, board[i][j], 1)
            visited[i][j] = False

            exce(i, j)

    print(maxValue)
