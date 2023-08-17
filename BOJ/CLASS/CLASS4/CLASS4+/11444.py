
'''
    백준 11444. 피보나치 수 6
    피보나치 수를 10억 7로 나눈 값을 출력하는 문제
'''

import sys
input = sys.stdin.readline

def solution():

    '''
        나의 풀이(내가 푼건 아님 ㅋㅋㅋ)

        나의 접근법
        피보나치를 1000 천조 자리까지 구해야해서... 1도 모르겠어서
        구글에 피보나치를 검색해보니까
        나무위키에 log n 으로 구하는 방법이 있다고 해서 봄
        
        그래서 그 방법을 사용해봄
        초기 행렬 [[1, 1], [1, 0]] ^ n 을 하면 n 번째 피보나치 수를 구할 수 있어서
        해당 공식을 사용하고

        ^ n 을 빠르게 구하는 방법은
        n 을 이진수로 나타내고 해당 자리수에 해당하는 걸 곱해주면됨
        ex) 43 = 101011 = 1 x 2^5 + 0 x 2^4 + 1 x 2^3 + 0 x 2^2 + 1 x 2^1 + 1 x 2^0 = 32 + 8 + 2 + 1
        이렇게 나와서
        32 승 곱하기 8승 곱하기 2승 곱하기 1승 해주면 됨
        그렇게 천조 가 넘어가는 피보나치 n 번째를 구할 수 있음

        수학 모르면 절~~~~~~~~~~~~~~때 못풀듯 ㅋㅋㅋㅋ
    '''

    n = int(input())

    if n == 1:
        print(1)
        return
    
    if n == 2:
        print(1)
        return
    
    
    base = { 1 : [[1, 1], [1, 0]]}

    bin_n = bin(n)

    digit = 0
    answer_matrix = [[1, 1], [1, 0]]

    for i in range(len(bin_n) - 1, 1, -1):

        now_num = int(bin_n[i]) * (2 ** digit)
        
        if now_num != 0:

            if now_num not in base:
                make_base_matrix(base, now_num)
            

            answer_matrix = matrix_multiplication(answer_matrix, base[now_num])

        digit += 1

    print(answer_matrix[1][1])

    return 

def make_base_matrix(base, n):

    
    while n not in base:
        
        now_max_n = list(base.keys())[-1]
        next_n = now_max_n * 2

        next_matrix = matrix_multiplication(base[now_max_n], base[now_max_n])

        base[next_n] = next_matrix
    




def matrix_multiplication(a, b):

    new_matrix = [[0, 0], [0, 0]]

    new_matrix[0][0] = ((a[0][0] * b[0][0]) + (a[0][1] * b[1][0])) % 1_000_000_007
    new_matrix[0][1] = ((a[0][0] * b[0][1]) + (a[0][1] * b[1][1])) % 1_000_000_007

    new_matrix[1][0] = ((a[1][0] * b[0][0]) + (a[1][1] * b[1][0])) % 1_000_000_007
    new_matrix[1][1] = ((a[1][0] * b[0][1]) + (a[1][1] * b[1][1])) % 1_000_000_007

    return new_matrix

solution()