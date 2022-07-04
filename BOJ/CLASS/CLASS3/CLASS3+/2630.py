white_count = 0
blue_count = 0

def checkWhiteAndBlueBoard(board, word):
    n = len(board)
    for temp in board:
        if temp != (n*word):
            return False
    return True


def splitBoard(board, divide, x, y):
    global white_count, blue_count

    if divide < 0:
        return

    split_board = []
    for now_y in range(y, y + divide):
        split_word = ''
        for now_x in range(x, x + divide):
            split_word += board[now_y][now_x]
        split_board.append(split_word)
    
    next_divide = int(divide / 2)

    if checkWhiteAndBlueBoard(split_board, '0'):
        white_count += 1
        return
    elif checkWhiteAndBlueBoard(split_board, '1'):
        blue_count += 1
        return

    splitBoard(split_board, next_divide, 0, 0) # 왼상
    splitBoard(split_board, next_divide, next_divide, 0) # 오상
    splitBoard(split_board, next_divide, 0, next_divide) # 왼하
    splitBoard(split_board, next_divide, next_divide, next_divide) # 오하

    return



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
#     [0, 0, 1, 1, 1, 1, 1, 1]]



str_board = []
for temp in board:
    str_board.append(str(''.join(map(str, temp))))

# str_board = ['1111',
# '1111',
# '1111',
# '1111']

next_div = int(N/2)

if checkWhiteAndBlueBoard(str_board, '0'):
    white_count += 1
elif checkWhiteAndBlueBoard(str_board, '1'):
    blue_count += 1
else:
    splitBoard(str_board, next_div, 0, 0)
    splitBoard(str_board, next_div, next_div, 0)
    splitBoard(str_board, next_div, 0, next_div)
    splitBoard(str_board, next_div, next_div, next_div)

print(white_count)
print(blue_count)