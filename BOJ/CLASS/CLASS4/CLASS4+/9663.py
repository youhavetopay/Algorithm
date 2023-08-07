
'''
    백준 9663. N-Queen 
    N x N 체스판에 서로 공격하지 못하게 N 개의 퀸을 놓는
    경우의 수를 계산하는 문제
'''

import sys
input = sys.stdin.readline


N = int(input())

answer = 0

def solution():

    '''
        나의 풀이

        나의 접근법
        몇일 전에 N-Queen 문제를 프로그래머스에서 풀어서
        쉽게 접근했는데 시간초과가 뜨길래 확인해보니까
        여기는 N 의 제한이 15 까지였음 ㅋㅋ
        그래서 set 에 현재 놓은 퀸의 x 값들을 넣어줘서
        약간 최적화를 해줬는데도 시간초과가 뜰 것 같아서
        질문게시판을 보니까 pypy3 으로 하면 통과한다고 해서
        해보니 통과 ㅋㅋ

        앞으론 pypy3 으로만 해야할 듯 ㅋㅋ
    '''

    def dfs(now_queen_locs, q_x, now_y):

        global N, answer

        if now_y >= N:
            if len(now_queen_locs) == N:
                answer += 1
            return

        for x in range(N):
            if x not in q_x and check(now_queen_locs, x, now_y):
                now_queen_locs.append([x, now_y])
                q_x.add(x)
                dfs(now_queen_locs, q_x, now_y + 1)
                now_queen_locs.pop()
                q_x.remove(x)
    

    def check(queen_locs, x, y):

        for q_x, q_y in queen_locs:
            if abs(q_x - x) == abs(q_y - y):
                return False
            
        return True

    dfs([], set(), 0)

    print(answer)


def firstSolu():

    '''
        다른 사람 풀이
        https://seongonion.tistory.com/103

        나랑 똑같은 방식으로 하심
        대신 1차원 배열에 저장을 해서 인덱스를 y 로 하고 해당 값을 x 로 하는 방식

        그리고 nonlocal 이라는 걸 알았는데
        내부함수에서 바깥쪽에 있는 지역변수를 사용할때 사용한다고 함
        디게 좋은듯
        이거 때문에 맨날 리스트로 선언해서 했었는데 이거 사용하면 좋을 듯 ㅋㅋㅋ
    '''
    
    n = int(input())

    ans = 0
    row = [0] * N
    
    def is_promising(x):
        for i in range(x):
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
                return False
            
        return True
    
    def n_queen(x):
        nonlocal ans

        if x == n:
            ans += 1
            return
        else:

            for i in range(n):
                row[x] = i
                if is_promising(x):
                    n_queen(x + 1)

    
    n_queen(0)
    print(ans)