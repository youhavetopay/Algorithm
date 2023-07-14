
'''
    백준 15650. N과 M(2)

    N, M 이 주어지면 만족하는 수열을 구하는 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def solution(n, m):

    '''
        나의 풀이

        나의 접근법
        만족하는 수열이 1 ~ N 까지 중복없이 오름차순으로 M 개를 선택하는 거라서
        dfs 로 구함

        dfs 응용문제 기본인듯??
    '''

    nums = []

    def dfs(now, last):
        if len(now) == m:
            nums.append(now)
            return
        
        for next in range(last+1, n+1):
            dfs(now + [next], next)

    for i in range(1, N+1):
        dfs([i], i)

    for num in nums:
        print(' '.join(map(str, num)))

    return

solution(N, M)


def firstSolu():

    '''
        다른 사람 풀이
        https://jiwon-coding.tistory.com/22

        나랑 똑같이 DFS로 숫자 찾아서 넣어줌
        대신 차이점은 append, pop 하면서 
        하나의 숫자 배열을 가지고 함
        
        문제 푸는덴 큰 차이는 없지만 메모리 측면에선 이게 더 좋을듯??
    '''

    n, m = list(map(int, input().split()))
    s = []

    def dfs(start):
        if len(s) == m:
            print(' '.join(map(str, s)))
            return
        
        for i in range(start, n + 1):
            if i not in s:
                s.append(i)
                dfs(i + 1)
                s.pop()
    
    dfs(1)