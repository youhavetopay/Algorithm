
'''
    백준 10830. 행렬 제곱
    행렬이 주어지면 B 제곱 을 구하는 문제
'''

import sys
input = sys.stdin.readline

def mul_array(A, B):

    new_array = []
    length = len(A)

    for z in range(length):
        row = []
        for i in range(length):
            num = 0
            for j in range(length):
                num += A[z][j] * B[j][i]
            
            row.append(num % 1000)
        new_array.append(row)
    
    return new_array

def make_base(base, target):

    # 목표 지수를 만들때까지 반복
    while target not in base:
        now_max_i = list(base.keys())[-1]
        next_i = now_max_i * 2

        next_array = mul_array(base[now_max_i], base[now_max_i])

        base[next_i] = next_array



def solution():

    '''
        나의 풀이

        나의 접근법
        B가 최대 1000억 이라서 
        저번에 제곱을 빠르게 구하는 방법을 이용함(피보나치 6)

        B를 2진수로 나타내고 해당 자리수의 하위 지수를 곱해서 구해주는 방법

        근데 최근에 비슷한 문제를 풀었음에도
        헷갈려서 헤메다가 결국 이전 풀이 보고 품.........

        그리고 희한한건 이건 왜 골드 4인지 이해가 안감 ㅋㅋㅋㅋ
    
    '''

    N, B = map(int, input().split())

    array = [list(map(int, input().split(' '))) for _ in range(N)]

    # 지수를 2진수로 나타내기
    bin_B = bin(B)

    # 단위 행렬 만들어두기
    # 행렬 ^ 0 = 단위 행렬
    unit_array = [[0] * N for _ in range(N)]
    for i in range(N):
        unit_array[i][i] = 1

    # 지수에 따른 행렬
    base = {0:unit_array, 1:array}

    # 정답
    answer = unit_array


    idx = 0
    for i in range(len(bin_B)-1, 1, -1):

        if bin_B[i] == '1':
            
            now_digit = int(bin_B[i]) * (2 ** idx)

            # 해당 지수가 없으면 만들어주기
            if now_digit not in base:
                make_base(base, now_digit)
            
            # 행렬 곱해주기
            answer = mul_array(answer, base[now_digit])
        
        idx += 1

    for row in answer:
        print(*row)

    return

solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10830-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1-%EA%B3%A8%EB%93%9C4-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

        거듭제곱을 분할정복으로 풀어내심

        n 이 짝수 일 때
        A^n = A^(n//2) * A^(n//2)
        n 이 홀수면
        A^n = A^(n//2) * A^(n//2) * A

        이런식으로 하심
    '''

    N, B = map(int, input().split())
    A = [[*map(int, input().split())] for _ in range(N)]

    def mul(U, V):
        n = len(U)
        Z = [[0] * n for _ in range(n)]

        for row in range(n):
            for col in range(n):
                e = 0
                for i in range(n):
                    e += U[row][i] * V[i][col]
                Z[row][col] = e % 1000
        
        return Z
    
    def square(A, B):
        if B == 1:
            for x in range(len(A)):
                for y in range(len(A)):
                    A[x][y] %= 1000

            return A
        
        tmp = square(A, B//2)
        if B % 2:
            return mul(mul(tmp, tmp), A)
        else:
            return mul(tmp, tmp)

    result = square(A, B)
    for r in result:
        print(*r)
