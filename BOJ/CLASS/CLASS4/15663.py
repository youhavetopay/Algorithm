
'''
    백준 15663. N과 M (9)

    주어진 수열에서 규칙에 만족하는 부분 수열을 출력하는 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

L = list(map(int, input().split()))

def solution(n, m, l):

    '''
        나의 풀이

        나의 접근법
        입력되는 수열에 중복이 있어서
        중복 수열을 방지하기 위해 값을 넣으면 안되고 해당 수열의 index를 넣어주고
        사전순으로 증가하게 출력해야해서
        넣은 순서를 보장하는 dict에 넣어서 풀었음

        참고로 dict은 옛날 파이썬에서는 순서를 보장 안하는 것으로 알고 있어서
        orderdict??을 사용해야 하는 걸로 알고 있음

        N과 M 시리즈 문제가 재귀로 조합과 순열을 구하는 문제이고
        데이터 크기도 크지 않아서 연습 문제로 딱 좋은 문제인듯 함 ㅋㅋ
    '''

    l.sort()

    answers = {}

    def dfs(now):
        if len(now) == m:
            nums = [l[i] for i in now]
            answers[' '.join(map(str, nums))] = 1
            return
        
        for next_i in range(n):
            if next_i not in now:
                dfs(now + [next_i])
                

    dfs([])

    for answer in answers.keys():
        print(answer)

    return


solution(N, M, L)


def firstSolu():

    '''
        다른 사람 풀이
        https://honggom.tistory.com/111

        나랑 비슷하게 DFS로 했음
        근데 remember_me 라는 것을 통해 중복 수열을 방지함 ㄷㄷㄷ
        입력되는 수열에서 중복이 있으므로 이것을 방지하기 위해 사용하신듯 ㄷㄷ

        난 파이썬 자료구조 이용했는데 ㄷㄷ

        이렇게 자료구조 이용 하지 않고 알고리즘으로 해결하는 방법이
        디게 대단한듯 
    '''

    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    visited = [False] * n
    temp = []

    def dfs():
        if len(temp) == m:
            print(*temp)
            return
        
        remember_me = 0
        for i in range(n):
            if not visited[i] and remember_me != nums[i]:
                visited[i] = True
                temp.append(nums[i])
                remember_me = nums[i]
                dfs()
                visited[i] = False
                temp.pop()
    
    dfs()