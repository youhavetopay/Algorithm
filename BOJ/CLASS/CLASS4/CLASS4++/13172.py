
'''
    백준 13172. Σ
    주사위 종류에 따른 기대값의 합을 계산하는 문제
    분수일때는 모듈러 곱셈에 대한 역원을 구해서 나타내기
'''

import sys
input = sys.stdin.readline

sys.setrecursionlimit(100_000)

def get_moduler(N, S):

    num = get_power(N, 1_000_000_005)

    return (S * num ) % 1_000_000_007

def get_power(num, exponet):

    if exponet == 0:
        return 1

    if exponet == 1:
        return num

    total_num = get_power(num, exponet // 2)
    if exponet % 2 == 0:
        return (total_num * total_num) % 1_000_000_007
    else:
        return ((total_num * total_num) * num) % 1_000_000_007
    

def solution():

    '''
        나의 풀이(온전히 내가 푼건 아님..)

        나의 접근법

        모듈러 곱셈의 역원이 이해가 안되서 뭔지 검색해보니까
        x에 대해 어떤 수(y)를 곱했을때 어떤 수(z)로 나눴을때 나머지가 1 인 어떤 수(y)를 의미 ㅋㅋㅋ

        이걸 원래대로 구하면 1 ~ z-1 까지 하나씩 찾아봐야 하는데
        만약 z 가 소수라면 x^z-2 가 모듈러 곱셈의 역원임

        그래서 분할정복으로 거듭제곱을 구하고
        모든 주사위의 기대값을 통분해주면서 구해주면 됨

        처음엔 주사위의 기대값을 더해주려고
        분모들의 최소 공배수를 구하려고 했는데 해보니까
        자꾸 메모리 초과가 뜨길래 질문하기를 보니까
        기대값들을 더해주는 과정에서도 수가 커질 수가 있어서
        10억7로 나눠줘야 한다고 함
        그래서 a/x + b/y = (ay + bx) / xy 를 이용해서 분모, 분자 모두 10억 7로 나눠주면서
        해줘야 함

        문제를 푸는 것 보다 문제를 이해하는게 더 어려웠던 문제.. ㅋㅋㅋ
        그리고 수학 모르면 절~~~~~~~~~~~~~~~~~~대 못풀듯 ㅋㅋㅋ
    '''

    M = int(input())

    dice = []

    for _ in range(M):
        N, S = map(int, input().split())
        dice.append([S, N])


    total_s = dice[0][0]
    total_n = dice[0][1]

    # 통분해주면서 모두 더해주기
    # a/x + b/y = (ay + bx) / xy
    for i in range(1, M):
        total_s = ((total_s * dice[i][1]) + (dice[i][0] * total_n)) % 1_000_000_007
        total_n = (total_n * dice[i][1]) % 1_000_000_007

    
    print(get_moduler(total_n, total_s))

    return

solution()

