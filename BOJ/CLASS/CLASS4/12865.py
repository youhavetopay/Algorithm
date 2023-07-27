
'''
    백준 12865. 평범한 배낭
    0-1 배낭 문제
'''

import sys
input = sys.stdin.readline

# N, K = map(int, input().split())

weight_and_value = []

# for _ in range(N):
#     w, v = map(int, input().split())
#     if v <= K:
#         weight_and_value.append([w, v])


N, K = 10, 15

weight_and_value = [
    [1, 1],
    [2, 3],
    [5, 3],
    [5, 1],
    [4, 5],
    [3, 3],
    [3, 2],
    [4, 4],
    [4, 4],
    [4, 3]
]


def solution(n, k, weight_and_value):

    '''
        나의 풀이(못품 ㅋㅋ)

        나의 접근법
        배낭문제 이라는 걸 알고 있었는데
        푸는 법은 몰라서 한참 헤메다가 결국 답 봄 ㅋㅋ

        처음엔 백트래킹 문제라고 생각해서
        완전탐색으로 구현하다가 도저히 중간에 끝낼 방법을 못찾아서
        알고리즘 유형을 봤는데 DP 라고 했음 ㅋㅋㅋㅋ

        그래서 점화식을 도출해보려고 했는데
        왜 DP 인지 이해가 안되서 결국 포기....

        물건의 개수와 배낭의 최대 크기를 2차원 배열로 나타낸후 -> 물건개수 X 배낭 최대 크기 의 행렬

        (i = 현재 물건번호, w = 현재 가방 최대 크기)
        dp[i][w] 은
        현재 물건을 담을 수 있을때 -> weight[i] < w
            max(dp[i-1][w-weight[i]] + value[i], dp[i-1][w])
            dp[i-1][w-weight[i]] : 현재 물건을 담을 수 있게 공간을 만든 가방의 최대값
            dp[i-1][w] : i 번째 물건을 포함하지 않은 값
        담을 수 없을때 -> weight[i] > w
            dp[i-1]

        이렇게 진행됨 ....

        이걸 어찌알아, ㅋㅋㅋㅋ
        1차원 배열의 DP 문제는 어찌저찌 풀어보겠는데
        2차원 배열의 DP 문제는 너무 어려움..
        많이 안풀어본것도 있지만 떠올리기 너무 어려움..(LCS 같은 문제나 배낭문제)
        
    '''

    dp = [ [0] * (k+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(k+1):
            weight = weight_and_value[i-1][0]
            if i == 0 or w == 0:
                dp[i][w] = 0
            
            elif w < weight:
                dp[i][w] = dp[i-1][w]
            else:
                value = weight_and_value[i-1][1]
                dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w])


    return dp[n][k]

print(solution(N, K, weight_and_value))


def firstSolu():

    '''
        다른 사람 풀이
        https://claude-u.tistory.com/208

        똑같은 풀이임
        문제가 워낙 유명해서 풀이법도 똑같은듯?? ㅋㅋ

        대신 stufff(물건 정보) 에 맨 앞에 [0, 0]을 너어줘서
        인덱스 에러 를 피해서 그런지 훨씬 코드가 깔끔함 ㅋㅋ
    
    '''

    N, K = map(int, input().split())
    stuff = [[0, 0]]
    knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for _ in range(N):
        stuff.append(list(map(int, input().split())))

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            weight = stuff[i][0]
            value = stuff[i][1]

            if j < weight:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

    print(knapsack[N][K]) 