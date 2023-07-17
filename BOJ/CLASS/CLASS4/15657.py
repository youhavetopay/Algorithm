
'''
    백준 15657. N과 M (8)
    주어진 조건에 따른 수열을 출력하는 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))

def solution(N, M, L):

    '''
        나의 풀이

        나의 접근법
        이번에는 백준 15654. N과 M(5) 보다 조금 더 업그레이드 된 문제
        고른 수열이 비내림차순이어야 함
        또한 같은 수도 선택해도 되기 때문에

        백준 15652. N과 M(4) 와 비슷하게 DFS로 품

        근데 문제 풀면서 좀 한심한게
        처음에 입력한 수열이 
        정답으로 출력되는 줄 알고 이게 왜 출력되지
        라고 한참 생각함... 으이구 ㅋㅋ
    '''

    L.sort()

    def dfs(now, last):
        if len(now) == M:
            print(' '.join(map(str, now)))
            return
        
        for i in range(last, N):
            dfs(now + [L[i]], i)

    dfs([], 0)

    return

solution(N, M, L)


def firstSolu():

    '''
        다른 사람 풀이
        https://honggom.tistory.com/110

        나랑 똑같이 DFS로 하심
        오 근데 리스트를 공백으로 나누면서 print 할때 * 쓰면 좋을듯? ㅋㅋ
    '''

    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    temp = []

    def dfs(start):
        if len(temp) == m:
            print(*temp)
            return
        
        for i in range(start, n):
            temp.append(nums[i])
            dfs(i)
            temp.pop()

    dfs(0)