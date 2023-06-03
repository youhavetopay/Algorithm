def count_board(board):

    o_count = 0
    x_count = 0

    for line in board:
        for value in line:
            if value == 'O':
                o_count += 1
            elif value == 'X':
                x_count += 1
    
    return [o_count, x_count]

def check_board(board, value):

    check_value = value * 3

    for line in board:
        if line == check_value:
            return True
        
    for i in range(len(board[0])):

        temp = ''
        for j in range(len(board)):
            temp += board[j][i]
        
        if temp == check_value:
            return True
    
    temp = ''
    for i in range(len(board)):
        temp += board[i][i]
    
    if temp == check_value:
        return True
    
    temp = ''
    for i in range(len(board)):
        temp += board[i][len(board) - 1 - i]
    
    if temp == check_value:
        return True
    
    return False

def solution(board):

    '''
        나의 풀이
        틱택토 게임을 할때 해당 결과가 나올 수 있는 결과인지
        체크하는 문제

        나의 접근법
        불가능한 경우만 체크하니까 풀림..
        O, X의 개수를 세고 게임이 완료됐는지를 체크함
        
        O, X의 개수가 같을때
        O으로 게임이 끝났으면 안됨

        O, X의 개수가 하나 차이일때
        X로 게임이 끝났으면 안됨

        두 문장의 개수가 아예 다르면 
        불가능함

        이 외에는 전부 가능함
        

        근데 테스트케이스가 엄~~~청 많네 ㅋㅋㅋㅋ

    '''

    o_count, x_count = count_board(board)

    if o_count == x_count:
        if check_board(board, 'O'):
            return 0
    
    elif o_count == x_count + 1:
        if check_board(board, 'X'):
            return 0

    else:
        return 0

    return 1




def check_win(player, board):

    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
    
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def firstSolu(board):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/160585/solution_groups?language=python3

        나랑 접근법 똑같음
        대신 파이썬 메소드를 참 잘 사용한듯..??(all 같은거)
        
    '''

    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0
    
    elif (check_win('O', board) and num_x != num_o - 1) or (check_win('X', board) and num_x != num_o):
        return 0
    
    return 1
