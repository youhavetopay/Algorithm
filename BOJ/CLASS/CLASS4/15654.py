
'''
    백준 15654. N과 M(5)
    정해진 조건에 만족하는 수열을 출력하는 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(input().rstrip().split())

def solution(N, M, nums):

    '''
        나의 풀이

        나의 접근법
        데이터 크기도 크지 않고 이전 문제랑 비슷한 부분이 많아서
        그냥 DFS로 구함

        근데 모르고 중복 제거를 안해서 한번 틀리고
        사전 순으로 정렬하라고 해서 그냥 문자열로 해서 하니까 틀렸다고 나오길래
        질문 게시판을 통해 반례를 봤는데
        그냥 숫자 오름 차순으로 정렬하라는 소리였음...

        그래서 숫자로 바꿔준 다음 오름차순으로 정렬하니 통과함..
        근데 이럴꺼면 그냥 숫자 오름차순이라고 하지 ㅋㅋ
        굳이 사전순이라고 해서 헷갈렸음 ㅋㅋ -> 아마 수열이라서 그런듯?? ㅋㅋㅋㅋ
    '''

    nums.sort()

    answers = set()

    def dfs(now):
        if len(now) == M:
            select_nums = [nums[idx] for idx in now]
            answers.add(' '.join(select_nums))
            return
        
        for next in range(N):
            if next not in now:
                dfs(now + [next])

    for i in range(N):
        dfs([i])
    
    
    sorted_answers = []
    for answer in answers:
        sorted_answers.append(list(map(int, answer.split())))
    
    sorted_answers.sort()
    for answer in sorted_answers:
        print(' '.join(map(str, answer)))

solution(N, M, nums)


def firstSolu():

    '''
        다른 사람 풀이
        https://wlstyql.tistory.com/62

        나랑 똑같이 DFS로 푸심
        
        이렇게 하는게 똑같은 풀이 방식이라해도
        훨씬 깔끔한듯??

        그리고 에초에 수열을 입력받을때
        숫자로 입력받고 정렬해주면 
        굳이 set에다 넣어서 정렬해줄 필요가 없어지네.. ㅋㅋㅋㅋ
        메모리도 줄이고 시간도 200 ms 더 줄음 ㅋㅋ
    '''

    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    L.sort()
    visited = [False] * N
    out = []

    def solve(depth, N, M):
        if depth == M:
            print(' '.join(map(str, out)))
            return
        
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                out.append(L[i])
                solve(depth + 1, N, M)
                out.pop()
                visited[i] = False
    
    solve(0, N, M)