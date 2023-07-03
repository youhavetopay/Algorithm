def solution(rows, columns, queries):

    '''
        나의 풀이
        주어진 범위의 행렬을 한칸씩 돌린 후
        돌린 행렬의 최소값을 찾는 문제

        나의 접근법
        최대 행렬크기가 100 * 100 이라서
        그냥 직접 행렬을 돌려서 확인함

        근데 생각보다 돌리는게 어려워서 좀 힘들었음ㅋ ㅋ

        그리고 rows, columns를 반대로 해서 헷갈렸음 ㅋㅋ

    '''

    answer = []

    board = [ [i + (columns * j) for i in range(1, columns+1)] for j in range(0, rows)]
    
    for r in board:
        print(r)

    for y1, x1, y2, x2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        answer.append(rotate_board([x1, y1], [x2, y2], board))

    return answer

def rotate_board(start, end, board):

    start_x, start_y = start
    end_x, end_y = end

    # 돌릴 부분 가져오기
    top_row = board[start_y][start_x:end_x+1]
    right_column = [board[i][end_x] for i in range(start_y, end_y+1)]
    bottom_row = board[end_y][start_x:end_x+1]
    left_column = [board[i][start_x] for i in range(start_y, end_y+1)]
    
    # 돌려주기
    left_column.pop(0)
    top_row.insert(0, left_column[0])

    top_row.pop()
    right_column.insert(0, top_row[-1])

    right_column.pop()
    bottom_row.append(right_column[-1])

    bottom_row.pop(0)
    left_column.append(bottom_row[0])


    # 돌린 행렬 넣어주기
    for i in range(len(top_row)):
        board[start_y][start_x+i] = top_row[i]

    for i in range(len(right_column)):
        board[i+start_y][end_x] = right_column[i]

    for i in range(len(bottom_row)):
        board[end_y][start_x+i] = bottom_row[i]

    for i in range(len(left_column)):
        board[i+start_y][start_x] = left_column[i]

    # 돌린 행렬의 최소 값 가져오기
    min_num = min(min(top_row), min(left_column), min(right_column), min(bottom_row))

    return min_num

# print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))

# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))

print(solution(100,	97,	[[1,1,100,97]]))


def firstSolu(rows, columns, queries):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/77485/solution_groups?language=python3

        스택을 사용해서 rotate를 구현하신 듯 함 ㅋㅋ
        훨씬 간단한듯 
    '''

    answer = []

    board = [[i + (j) * columns for i in range(1, columns+1)] for j in range(rows)]

    for a, b, c, d in queries:
        stack = []

        r1, c1, r2, c2 = a-1, b-1, c-1, d-1

        for i in range(c1, c2 + 1):
            stack.append(board[r1][i])

            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]
            
        
        for j in range(r1 + 1, r2 + 1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]
        
        for k in range(c2 - 1, c1 - 1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]
        
        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))

    return answer


from collections import deque
def secondSolu(rows, columns, queries):

    '''
        두번째 다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/77485/solution_groups?language=python3

        deque를 활용한 풀이
        deque에 rotate 라는 기능이 있었음 ㄷㄷㄷ
        회전 시킬 숫자들을 전부 answer에 넣고 
        1번 회전시킨 다음 -> (뺴고 넣고 한번 인듯??)
        넣어주면 됨 ㄷㄷ

    '''

    arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]

    answer, result = deque(), []

    for i in queries:

        a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1

        for x in range(d-b):
            answer.append(arr[a][b+x])

        for y in range(c-a):
            answer.append(arr[a+y][d])

        for z in range(d-b):
            answer.append(arr[c][d-z])

        for k in range(c-a):
            answer.append(arr[c-k][b])

        answer.rotate(1)
        result.append(min(answer))

        for x in range(d-b):
            arr[a][b+x] = answer[0]
            answer.popleft()

        for y in range(c-a):
            arr[a+y][d] = answer[0]
            answer.popleft()

        for z in range(d-b):
            arr[c][d-z] = answer[0]
            answer.popleft()

        for k in range(c-a):
            arr[c-k][b] = answer[0]
            answer.popleft()

    return result