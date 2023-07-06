
'''
    백준 20529. 가장 가까운 세 사람의 심리적 거리
    MBTI 리스트가 주어지면 세 사람(MBTI 중복 가능)의 
    심리적 거리가 가장 낮은 거리를 찾는 문제
'''

import sys
from collections import Counter
from itertools import combinations
input = sys.stdin.readline

def solution(mbtis):

    '''
        나의 풀이

        나의 접근법
        처음에 생각했을땐 최대 테스트 케이스의 합이 10만이라고 하길래
        완전탐색은 힘들겠다 라고 생각했는데
        다시 생각해보니 MBTI 종류가 16개 밖에 없고 10만개라고 하더라도 종류는 16개 밖에 없으니 
        3개를 뽑는 조합을 테스트 해보니 금방 출력되길래 조합으로 품 ㅋㅋ

        처음에 Counter로 중복을 제거하고 most_common으로 중복 값이 3명 이상이면 0
        MBTI 종류가 2개이면 해당 MBTI 끼리 계산

        나머지는 조합으로 전부 구함

        그렇게 하니까 풀림 ㅎㅎ
    '''

    # Counter로 중복 제거 및 카운팅
    counted_mbtis = Counter(mbtis)

    # 같은 MBTI 를 가진 사람이 3명 이상이면 0으로 끝내기
    if counted_mbtis.most_common(1)[0][1] >= 3:
        return 0
    
    # 최소 거리
    min_dist = float('inf')

    # MBTI 가지수가 2개 일때 -> 가지수가 하나면 위에서 걸림 -> 최소 입력수가 3
    if len(counted_mbtis.keys()) < 3:
        temp_mbti = list(counted_mbtis.keys())
        first_dist = get_dist(temp_mbti[0], temp_mbti[1])
        second_dist = get_dist(temp_mbti[1], temp_mbti[0])

        min_dist = min(min_dist, min(first_dist * 2, second_dist * 2))

    # 가지수가 3개 이상이면 조합으로 구하기
    for now_combi in list(map(set, combinations(counted_mbtis.keys(), 3))):
        now_combi = list(now_combi)


        # 같은 계산을 여러번 하긴 하는데 중복계산 안하려고 코드 나누면 그게 더 복잡할듯 ㅋㅋ
        for i, mbti in enumerate(now_combi):

            # 해당 mbti를 가진 사람이 두명이 있을때
            # A, A, B 해보고 A, A, C 해보기
            if counted_mbtis[mbti] == 2:
                
                first_dist = get_dist(mbti, now_combi[(i+1) % 3])
                second_dist = get_dist(mbti, now_combi[(i+2) % 3])

                min_dist = min(min_dist, min(first_dist * 2, second_dist * 2))

            # 한명 밖에 없을 때
            elif counted_mbtis[mbti] == 1:

                a_b_dist = get_dist(mbti, now_combi[(i+1) % 3])
                b_c_dist = get_dist(now_combi[(i+1) % 3], now_combi[(i+2) % 3])
                c_a_dist = get_dist(mbti, now_combi[(i+2) % 3])

                min_dist = min(min_dist, a_b_dist + b_c_dist + c_a_dist)

    return min_dist


def get_dist(a, b):

    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    
    return dist

T = int(input())

for _ in range(T):
    N = int(input())
    mbtis = list(map(str, input().split()))

    print(solution(mbtis))

# N = 5
# mbtis = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']


def fristSolu():

    '''
        다른 사람 풀이
        https://lem0nad3.tistory.com/9

        비둘기집 원리??  ㅋㅋㅋ 
        (n개보다 많은 물건은 n개의 집합으로 나눠넣으면 무조건 하나 이상에 중복이 있는 것)
        
        이거 때문에 입력 수가 32가 넘어가면 mbti가 같은 사람 3명이 무조건 있는 거임
        그래서 그 외에는 완전탐색으로 찾기

        알고리즘은 얼추 비슷한 것 같은데
        속도가 무슨 내꺼보다 10배정도 느림..
        Counter로 중복을 제거한게 확실히 크긴 큰듯??
        그리고 파이썬 라이브러리를 많이 사용해서 그런듯 함
    
    '''

    t = int(input())

    while t:

        ans = 99999999
        t -= 1
        n = int(input())
        a = list(map(str, input().split()))

        if n > 32:
            print(0)
        else:
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        tmp = 0
                        if i == j or j == k or i == k:
                            continue
                        for x in range(4):
                            if a[i][x] != a[j][x]:
                                tmp += 1
                            if a[j][x] != a[k][x]:
                                tmp += 1
                            if a[i][x] != a[k][x]:
                                tmp += 1
                        ans = min(tmp, ans)

            print(ans)



