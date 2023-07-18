
'''
    백준 15666. N과 M (12)
    주어진 수열에서 조건에 만족하는 부분 수열 출력하는 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

L = list(map(int, input().split()))


def solution(n, m, l):

    '''
        나의 풀이

        나의 접근법
        15663. N과 M (9) 문제에서 조금 더 업그레이드 된 문제
        중복 선택을 허용하고 비내림차순을 만족하는 수열을 찾는 문제

        그냥 수열 정렬하고 이전에 선택한 수열 부터 선택해 나가는 방식으로 품

        solved.ac 에 있는 N과 M 시리즈는 이게 마지막인듯??
        이제 이런문제 계속 푸니까 질린다.. ㅋㅋ
        
    '''

    l.sort()

    answers = {}

    def dfs(now, last):

        if len(now) == m:
            nums = [l[i] for i in now]
            answers[' '.join(map(str, nums))] = 1
            return
        
        for next in range(last, n):
            dfs(now + [next], next)
    
    dfs([], 0)

    for answer in answers.keys():
        print(answer)



    return

solution(N, M, L)


def firstSolu():

    '''
        다른 사람 풀이
        https://honggom.tistory.com/114

        15663 번 다른 사람 풀이랑 같은 사람 꺼 ㅋㅋ

        나랑 똑같이
        해당 코드에서 마지막으로 선택한 index를 추가해주는 방식으로 푸심
    '''

    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    temp = []

    def dfs(start):
        if len(temp) == m:
            print(*temp)
            return
        remember_me = 0
        for i in range(start, n):
            if remember_me != nums[i]:
                temp.append(nums[i])
                remember_me = nums[i]
                dfs(i)
                temp.pop()

    dfs(0)