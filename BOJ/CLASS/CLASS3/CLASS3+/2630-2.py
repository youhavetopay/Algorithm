'''
    나의 풀이

    분할정복해서 색상별 정사각형의 크기를 구하는 문제

    
    나의 접근법
    그냥 크기에 1/4 로 나누어서 체크하고
    계속 1/4로 나누어서 체크하는 방식으로 품
    

    이전에 풀었던 문제인데
    solved에 기록이 안되서 다시 품 ㅋㅋ

    예전에는 리스트를 굳이..?? 문자열로 합쳐서 분할정복을 함..??
    왜....?? ㅋㅋㅋㅋㅋ

'''



N = int(input())

board = []
for i in range(N):
    board.append(list(map(int, input().split(' '))))



# N = 8
# board = [

#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1]

# ]

answer = [0, 0]
WHITE = 0
BLUE = 1

# 색상 검증 함수
# 다른 색 들어가 있으면 False를 리턴함
def isColor(check_board, color_value):

    for temp in check_board:
        if color_value in temp:
            return False
    
    return True

def division(new_board):

    # 현재 board의 색상 검증
    if isColor(new_board, WHITE):
        answer[1] += 1
        return
    
    if isColor(new_board, BLUE):
        answer[0] += 1
        return
    
    # 나눌 수 있는지 체크
    if len(new_board) / 2 > 0:

        # 나눌 사이즈
        size = len(new_board) // 2
        
        # 왼쪽 상단, 오른쪽 상단, 왼쪽 하단, 오른쪽 하단으로 나누기
        left_top = []
        right_top = []
        for i in range(size):
            left_top.append(new_board[i][:size])
            right_top.append(new_board[i][size:size*2])

        left_down = []
        right_down = []
        for i in range(size, size*2):
            left_down.append(new_board[i][:size])
            right_down.append(new_board[i][size:size*2])
        
        # 재귀
        division(left_top)
        division(right_top)
        division(left_down)
        division(right_down)

    return

division(board)

for i in answer:
    print(i)










'''
    다른 사람 풀이
    https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python

    똑같이 분할정복해서 품
    대신 분할할때 각각의 시작 부분의 위치값을 넘겨줘서
    좀더 깔끔하게 하는듯함
    
    그에 비해 나의 풀이는 새로 리스트를 만들어서 공간복잡도가 조금 높을듯 함


    그리고 리스트에다가 0과 1을 넣어서 각각의 개수를 count해서 정답으로 출력함
    디게 신기하게 품 ㅎㅎ
'''


import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split()))  for _ in range(N)]

result = []

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                solution(x, y, N // 2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)
print(result.count(0))
print(result.count(1))