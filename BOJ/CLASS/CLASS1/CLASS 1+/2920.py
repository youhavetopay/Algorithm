'''
2920 음계 

연속된 배열인지 아닌지 판별하는 문제

'''

values = input()
    
list_values = list(map(int, values.split(' ')))

values_length = len(list_values)

flag = 0
for idx, value in enumerate(list_values):
    if 0 <= idx-1 and idx-1 < values_length:
        if value == list_values[idx-1] + 1: # 정 배열
            flag = 1
        elif value == list_values[idx-1] - 1: # 역 배열
            flag = -1
        else: # 정렬 아닌거
            flag = 0 
            break

if flag == 1:
    print('ascending')
elif flag == -1:
    print('descending')
else:
    print('mixed')