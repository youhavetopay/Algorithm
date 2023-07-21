
'''
    백준 9465. 스티커

    n x 2 배열이 있을 때
    점수의 최대 합을 구하는 문제
    단 스티커 하나를 선택하면 해당 스티커와 변이 닿고 있는 스티커는 
    다음에 선택을 못함
'''

import sys
input = sys.stdin.readline

def solution(n, stickers):

    '''
        나의 풀이

        나의 접근법

        처음에 또 아무 생각없이 DFS로 모든 경우의 수를 찾다가 시간초과로 실패함 ㅋㅋ

        그래서 보니 역시나 DP 였음..
        이전에 뭘 선택했냐에 따라 지금 선택할 수 있는 스티커가 달라지기 때문임

        점화식 찾는데 좀 애먹음 ㅋㅋㅋ

        현재껄 무조건 선택하는 것은 구현하기 쉬웠는데
        이번껄 선택 안하고 넘어가는 걸 구현하기 어려웠음 ..

        그냥 전전꺼 중에서 높은 값이랑 비교하면 되는 거였음..
    '''

    # DP 초기화
    dp = [
        [stickers[0][0], stickers[1][0]]
    ]

    # 두번째 선택 전까지는 이전 스티커를 선택안하는 걸 고려할 필요 없음
    if n > 1:
        for i in range(1, 2):

            # 현재 위, 아래의 스티커 선택
            # ex) 현재 위를 선택하면 이전꺼에서는 아래꺼를 선택했어야 가능함
            top = dp[i-1][1] + stickers[0][i]
            bottom = dp[i-1][0] + stickers[1][i]
            dp.append([top, bottom])

    # 두번째 선택 이후 부터
    if n > 2:
        for i in range(2, n):

            # 현재 위, 아래의 스티커 선택
            top = dp[i-1][1] + stickers[0][i]
            bottom = dp[i-1][0] + stickers[1][i]

            now_top = stickers[0][i]
            now_bottom = stickers[1][i]

            # N - 1 번째 스티커 선택 안하고 넘어온 경우
            last_max = max(dp[i-2])

            # N - 2 최대값과 현재 값을 가져오기
            notting_top = last_max + now_top
            notting_bottom = last_max + now_bottom

            # 최대값으로 넣어주기
            dp.append([max(top, notting_top), max(bottom, notting_bottom)])

    
    return max(dp[-1])


T = int(input())

for _ in range(T):
    N = int(input())
    sticker = [ list(map(int, input().split())) for _ in range(2)]

    print(solution(N, sticker))

# N = 10
# sticker = [
#     [0, 1, 1, 3, 3, 5, 4 ,6 ,6 ,0],
#     [1, 0, 0, 0, 0, 0, 0 ,0 ,0 ,10]
# ]

# print(solution(N, sticker))

def firstSolu():
    T = int(input())

    for _ in range(T) :
        n = int(input())
        dp = [list(map(int,input().split())) for _ in range(2)]

        if n > 1 :
            dp[0][1] += dp[1][0]
            dp[1][1] += dp[0][0]
            
        for i in range(2,N) :
            dp[0][i] += max(dp[1][i-1],dp[1][i-2])
            dp[1][i] += max(dp[0][i-1],dp[0][i-2])

        print(max(dp[0][n-1],dp[1][n-1]))