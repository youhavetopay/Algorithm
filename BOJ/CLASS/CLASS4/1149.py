
'''
    백준 1149. RGB거리

    각각의 집에 색을 칠하는데 연속적으로 같은 색을 칠 할 수 없을때
    모든 집에 색을 칠하는데 필요한 최소 비용을 구하는 문제
'''

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# N = int(input())

# color_costs = [list(map(int, input().split())) for _ in range(N)]

N = 8
color_costs = [
    [71, 39, 44],
    [32, 83, 55],
    [51, 37, 63],
    [89, 29, 100],
    [83, 58, 11],
    [65, 13, 15],
    [47, 25, 29],
    [60, 66, 19]
]

def solution(n, color_costs):

    '''
        나의 풀이

        나의 접근법
        DP 문제였음....
        처음엔 아무 생각없이 완전탐색으로 구현했는데
        시간초과가 떴었음
        그래서 생각해보니 3 * 2^999 의 경우의 수가 나와서 망했다 싶었음 ㅋㅋㅋ

        그러다가 알고리즘 유형을 봤는데 DP 라고 되어 있어서 
        이게 어떻게 DP지? 하고 곰곰히 생각해봤는데
        솔직히 문제 유형보고 억지로 끼워 맞춘거나 마찬가지 ㅋㅋㅋ

        일단 이전에 선택한 집 색깔에 따라서 현재 선택해야하는 집 색깔도 달라짐 -> 이전 결과값이 현재 값에 영향을 미침 (그래서 DP?)
        선택할 수 있는 색상이 3개 이므로 
        3 * N 형식의 배열을 만들고
        
        dp[n][0] 은 현재 빨간색 선택
        dp[n][1] 은 현재 초록색 선택
        dp[n][2] 은 현재 파란색 선택

        이런식으로 하고 
        
        지금 빨간색을 선택하면 이전에는 빨간색을 선택을 못하니
        이전 초록색 값과 파란색값 에 현재 빨간색의 값을 더해주고 
        둘 중의 최소값이 현재 빨간색을 선택했을때 최소값이 됨

        이런식으로 선택했던 비용의 최소 값을 더해주면 될듯하여 해보니
        통과 ㅋㅋ

        개인적으로 DP 문제는 많이 안풀어봐서 모르겠지만
        문제를 보고 이건 DP 로 풀어야겠다라는 생각이 잘 안듬..

        알고리즘 유형 못봤으면 혼자선 평생 못풀었을듯 ㅋㅋㅋㅋㅋ
    '''

    dp = []
    dp.append([0,0,0])

    i = 1
    while len(dp) <= n:

        red_pick = min(dp[i-1][1] + color_costs[i-1][0], dp[i-1][2] + color_costs[i-1][0])
        green_pick = min(dp[i-1][0] + color_costs[i-1][1], dp[i-1][2] + + color_costs[i-1][1])
        blue_pick = min(dp[i-1][0] + color_costs[i-1][2], dp[i-1][1] + color_costs[i-1][2])

        dp.append([red_pick, green_pick, blue_pick])
        i += 1

    return min(dp[n])


print(solution(N, color_costs))


def firstSolu():

    '''
        다른 사람 풀이
        https://namhandong.tistory.com/131

        나랑 똑같은 방식
        대신 배열을 새로 만드는게 아닌
        기존 색 칠하는 비용을 담아둔 배열에 바로 값을 바꿔줌
        그리고 min 하는 부분을 깔끔하게 정리한듯? ㅋㅋ
    '''

    n = int(input())
    RGB = []

    for i in range(n):
        RGB.append(list(map(int, input().strip().split())))
    
    for i in range(1, n):
        RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]

        RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]

        RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]
    
    print(min(RGB(n-1)))