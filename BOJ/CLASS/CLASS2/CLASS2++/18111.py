import sys
input = sys.stdin.readline

N, M, B = map(int, input().split(' '))

home_board = []
for i in range(N):
    input_line = list(map(int, input().split(' ')))
    home_board.append(input_line)

# N, M, B = 3, 4, 11
# home_board = [[29, 51, 54, 44],

# [22, 44, 32, 62],

# [25, 38, 16, 2]]

max_height = 256

answer_time = 99999999999999999
answer_height = 0


while max_height >= 0:

    now_B = B

    remove_block = 0
    fill_block = 0

    for board in home_board:
        for rand in board:
            if max_height - rand > 0:
                fill_block += (max_height - rand)
            elif max_height - rand < 0:
                remove_block += (rand - max_height)
    
    now_B += remove_block

    if now_B < fill_block:
        max_height -= 1
        continue

    total_time = (remove_block * 2) + fill_block
    if answer_time > total_time or (answer_time == total_time and answer_height < max_height):
        answer_time = total_time
        answer_height = max_height
    
    max_height -= 1

print(answer_time, answer_height)