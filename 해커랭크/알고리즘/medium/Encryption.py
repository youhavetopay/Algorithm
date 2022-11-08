import math


def encryption(s):
    # Write your code here
    
    answer = ''
    
    s = s.replace(' ', '')
    
    length = len(s)
    
    rows = math.floor(length ** 0.5)
    columns = math.ceil(length ** 0.5)
    


    if rows * columns < length:
        rows += 1

    print(length, rows, columns)

    board = []
    tempS = ''
    count = 0
    for index, value in enumerate(s):
        tempS += value
        count += 1
        if count == columns:
            count = 0
            board.append(tempS)
            tempS = ''
            
    if tempS != '':
        board.append(tempS)
    print(board)
    
    for i in range(columns):
        for j in range(rows):
            try:
                answer += board[j][i]
            except:
                continue
        
        answer += ' '
    return answer[:-1]

print(encryption('iffactsdontfittotheorychangethefacts'))