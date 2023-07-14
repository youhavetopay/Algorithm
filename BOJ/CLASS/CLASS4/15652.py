
'''
    백준 15652. N과 M(4)

    N, M 이 주어지면 만족하는 수열을 구하는 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def solution(n, m):
    
    '''
        나의 풀이
        
        나의 접근법
        백준 15650. N과 M(2) 문제에서 조금 업그레이드 된 문제

        중복 허용해서 비내림차순? 으로 출력하면 됨
        비내림차순은 같으면서 큰 순으로 정렬한것

        그냥 중복허용하도록 조금 바꿈
        그리고 배열에 담지말고 바로 출력하는 방식으로
        바꿔봄 ㅎㅎ

    '''

    def dfs(now, last):
        if len(now) == m:
            print(' '.join(map(str, now)))
            return
        
        # 15650 과 다른점은 여기
        # 중복을 허용하도록 이전에 선택했던 부분 부터 시작
        for next in range(last, n+1):
            dfs(now + [next], next)
    
    for i in range(1, n + 1):
        dfs([i], i)

solution(N, M)


def firstSolu():

    '''
        다른 사람 풀이
        https://jiwon-coding.tistory.com/24

        15650. N과 M(2) 때 다른 사람 이랑 똑같은 사람 ㅋㅋㅋㅋ
        역시나 이 분도 나랑 똑같이 품 ㅋㅋ
    '''

    n,m = map(int, input().split())
 
    s = []
    
    def dfs(start):
        if len(s)==m:
            print(' '.join(map(str,s)))
            return
        
        for i in range(start, n+1):
            s.append(i)
            dfs(i)
            s.pop()
        
    dfs(1)