
'''
    백준 15686. 치킨 배달
    치킨집 중 N개를 선택했을때 도시의 치킨거리가 최소가 되는 값을 구하는 문제
'''

import sys
input = sys.stdin.readline

from itertools import combinations

def solution():

    '''
        나의 풀이

        나의 접근법
        처음엔 BFS를 해야하나 생각했었는데
        그럴 필요가 없었음.. ㅋㅋㅋ

        일단 집 위치랑 치킨집 위치를 따로 저장해두고
        조합을 통해서 현재 선택한 치킨집의 인덱스에 따라 도시의 치킨 거리를 계산해주면서
        비교하면 풀리는 문제였음 ㅎㅎ

        집 수는 최대 100개 이고 치킨집 수도 최대 13개 이기 때문에 
        for 문으로도 쉽게 쉽게 풀리는 듯 함 ㅎㅎ
    '''

    N, M = map(int, input().split())


    houses = []
    chickens = []

    for y in range(N):
        row = list(map(int, input().split()))
        
        for x, kind in enumerate(row):
            if kind == 1:
                houses.append([x, y])
            elif kind == 2:
                chickens.append([x, y])

    total_min_chicken_dist = float('inf')
    for selected_chicken in list(combinations([ i for i in range(len(chickens))], M)):

        now_min_chicken_dist = 0

        for house in houses:

            chicken_dist = float('inf')

            for chicken_i in selected_chicken:
                chicken_dist = min(chicken_dist, abs(house[0] - chickens[chicken_i][0]) + abs(house[1] - chickens[chicken_i][1]))

            
            now_min_chicken_dist += chicken_dist
        
        total_min_chicken_dist = min(total_min_chicken_dist, now_min_chicken_dist)

    print(total_min_chicken_dist)
    return

solution()

def firstSolu():

    '''
        다른 사람 풀이
        https://codesyun.tistory.com/185

        나랑 똑같은 풀이 ㅋㅋㅋㅋ
        combinations 사용해서 똑같이 풀어냄 ㅋㅋㅋ
    '''

    n, m = map(int, input().split())
    city = list(list(map(int, input().split())) for _ in range(n))

    result = 999999
    house = []
    chick = []

    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house.append([i, j])
            elif city[i][j] == 2:
                chick.append([i, j])
    

    for chi in combinations(chick, m):
        temp = 0

        for h in house:
            chi_len = 999
            for j in range(m):
                chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][i]))
            
            temp += chi_len
        
        result = min(result, temp)

    print(result)