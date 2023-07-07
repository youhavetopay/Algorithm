
'''
https://www.acmicpc.net/board/view/109610
반례 모음집 ㅋㅋ
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

wrong_buttons = []
if M > 0:
    wrong_buttons = list(map(int, input().split()))
    
# N = 500000
# M = 6
# wrong_buttons = [0, 1, 2, 3, 4 ,5]

can_push_buttons = []

for i in range(0, 10):
    if i not in wrong_buttons:
        can_push_buttons.append(i)

min_push_count = abs(N - 100)

def solution():
    global N, M
    
    if N == 100:
        return 0
    
    if len(wrong_buttons) == 10:
        return abs(100 - N)
    
    if abs(N - 100) >= len(str(N)) and len(wrong_buttons) == 0:
        return len(str(N))

    
    min_max_num = ''
    max_min_num = ''
    reversed_N = list(str(N))
    

    flag = False
    for num in reversed_N:
        
        if flag == True:
            min_max_num += str(can_push_buttons[-1])
            continue

        for i in range(len(can_push_buttons)):
            if can_push_buttons[i] > int(num):
                min_max_num += str(can_push_buttons[i-1])
                if can_push_buttons[i-1] != int(num):
                    flag = True
                break
            elif can_push_buttons[i] == int(num):
                min_max_num += str(can_push_buttons[i])
                break
        else:
            min_max_num += str(can_push_buttons[-1])
            if can_push_buttons[-1] != int(num):
                flag = True
                    

    flag = False
    for num in reversed_N:
        
        for i in range(len(can_push_buttons)):
            if flag == True and can_push_buttons[i] <= int(num):
                max_min_num += str(can_push_buttons[i])
                break
            if can_push_buttons[i] > int(num):
                max_min_num += str(can_push_buttons[i])
                flag = True
                break
        else:
            max_min_num += str(can_push_buttons[-1])
    
    str_max_min = ''.join(reversed(list(max_min_num)))
    if int(str_max_min) < N:
        str_max_min += str(can_push_buttons[0])
    
    min_max_num = int(min_max_num)
    max_min_num = int(str_max_min)
    if min_max_num == 0:
        min_max_num += 1
    print(min_max_num, max_min_num)
    print(min_push_count, abs(N - min_max_num) + len(reversed_N), abs(N-max_min_num)+ len(reversed_N))
    return min(min_push_count, abs(N - min_max_num) + len(reversed_N), abs(N-max_min_num)+ len(reversed_N))


print(solution())