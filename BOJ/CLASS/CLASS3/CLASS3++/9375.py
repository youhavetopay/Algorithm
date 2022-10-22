import sys
input = sys.stdin.readline


def solution(clothes, N):
    
    total_day = 1
    for key, value in clothes.items() :
        total_day *= (value + 1)
    
    print(total_day - 1)
    

T = int(input())

while T > 0:

    N = int(input())
    clothes = {}
    for _ in range(N):
        name, position = map(str, input().strip().split(' '))

        try:
            clothes[position] += 1
        except KeyError:
            clothes[position] = 1

    # N = 6
    # clothes = {
    #     'g':['a', 'b', 'c',],
    #     'h' : ['d', 'e'],
    #     'f':['i']
    # }

    solution(clothes, N)

    T -= 1