
'''
    백준 2096. 내려가기
    RGB 거리 문제랑 비슷한 문제
    아래 줄로 내려가는데 이전에 선택한 곳에 따라 이번에 선택할 수 있는 수가 달라짐
    그렇게 계속 내려가면서 얻은 점수의 최대랑 최소 둘다 구해야하는 문제
'''

import sys
input = sys.stdin.readline

'''
    나의 풀이

    나의 접근법
    RGB 거리 문제랑 똑같은데
    최소 값도 구해야해서 그냥 DP 두번을 했고 평상시 하는 것 처럼
    solution 함수 만들어서 했는데 메모리 초과 뜨길래 뭐지 싶었음 ㅋㅋㅋ

    어차피 바로 이전에 값만 필요하기 때문에 리스트에 모든 이전값을 저장하지 않고
    메모리 사용량 줄일려고 리스트를 하나도 안쓰고 함수 호출안하고 바로 하도록
    깡으로 다 적음 ㅋㅋ
'''

N = int(input())

last_min_a, last_min_b, last_min_c = -1, -1, -1
now_min_a, now_min_b, now_min_c = -1, -1, -1

last_max_a, last_max_b, last_max_c = -1, -1, -1
now_max_a, now_max_b, now_max_c = -1, -1, -1

for _ in range(N):
    a, b, c = map(int, input().split())

    if last_min_a == -1:
        last_min_a, last_min_b, last_min_c = a, b, c
        last_max_a, last_max_b, last_max_c = a, b, c
        continue

    now_min_a, now_min_b, now_min_c = -1, -1, -1
    now_max_a, now_max_b, now_max_c = -1, -1, -1

    now_min_a = min(last_min_a, last_min_b) + a
    now_min_b = min(last_min_a, last_min_b, last_min_c) + b
    now_min_c = min(last_min_b, last_min_c) + c

    now_max_a = max(last_max_a, last_max_b) + a
    now_max_b = max(last_max_a, last_max_b, last_max_c) + b
    now_max_c = max(last_max_b, last_max_c) + c

    last_min_a, last_min_b, last_min_c = now_min_a, now_min_b, now_min_c
    last_max_a, last_max_b, last_max_c = now_max_a, now_max_b, now_max_c


print(max(last_max_a, last_max_b, last_max_c), min(last_min_a, last_min_b, last_min_c))


def firstSolu():

    '''
        다른 사람 풀이
        https://my-coding-notes.tistory.com/318

        풀이 알고리즘은 역시 똑같은데
        문제는 메모리 인듯 ㅋㅋ

        첫번째만 따로 입력 받아서 저장해두고
        그 다음 부턴 계속 재할당하는 방식으로 하심
        이게 훨~~~~~~~씬 깔끔한듯 ㅋㅋㅋ
    '''

    n = int(input())
    tmp = list(map(int, input().split()))
    dp1 = tmp
    dp2 = tmp

    for _ in range(n-1):
        a, b, c = map(int, input().split())
        dp1 = [a + max(dp1[0], dp1[1]), b + max(dp1), c + max(dp1[1], dp1[2])]
        dp2 = [a + min(dp2[0], dp2[1]), b + min(dp2), c + min(dp2[1], dp2[2])]
    
    print(max(dp1), min(dp2))