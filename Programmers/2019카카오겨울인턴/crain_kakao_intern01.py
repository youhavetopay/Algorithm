def solution(board, moves):
    answer = 0

    boardWidth = len(board)
    stack = []

    for i in moves:
        for j in range(boardWidth):
            
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                
                answer += 2
                del stack[-1]
                del stack[-1]
    return answer 


list1=[
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
list2 = [1,5,3,5,1,2,1,4]

solution(list1, list2)