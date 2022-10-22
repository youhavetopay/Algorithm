import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))

sum_list = [0]
length = 1

while M > 0:

    i, j = map(int, input().split(' '))
    
    while length-1 < j:
        sum_list.append(num_list[length-1] + sum_list[-1])
        length += 1
    
    print(sum_list[j] - sum_list[i-1])

    M -= 1