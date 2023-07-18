
'''
    백준 16953. A → B
    A 를 B 로 만들때 정해진 규칙에 따라
    증가 시킬때 최소 연산 횟수를 구하는 문제
'''

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def solution(a, b):

    '''
        나의 풀이
        
        나의 접근법
        입력의 최대 수가 10억 이긴 하지만
        최소로 증가하는게 x 2 라서 해봤자 2^30 만 되도 10억이 넘어가기 때문에
        깊이 30이 최대였음
        그리고 빼는 연산이 없기 때문에 현재 숫자가 넘어가면 끝내는 방식(백트래킹?) 으로 하니까
        풀렸음

        알고리즘 분류에는 너비 우선 탐색이 있긴 한데
        연산자체가 그렇게 많지 않고 빼는 연산이 없어서 훨씬 쉬운듯?? 
    '''

    min_answer = [float('inf')]

    def dfs(now, depth):

        if now == b:
            min_answer[0] = min(min_answer[0], depth)
            return
        
        # 숫자 넘어가면 끝내기
        if now > b:
            return
        
        # 곱하기 2 하는 연산이랑 
        # 자리수 하나 더 늘리는 연산
        dfs(now * 2, depth + 1)
        dfs(int(str(now) + '1'), depth + 1)
    
    dfs(a, 0)

    # 값을 만들지 못한 경우
    if min_answer[0] == float('inf'):
        return -1

    return min_answer[0] + 1

print(solution(A, B))


def firstSolu():

    '''
        다른 사람 풀이
        https://my-coding-notes.tistory.com/210

        top-down 방식으로 하심
        10 으로 나누는게 가장 빨라서
        맨 뒷자리가 1 이면 10으로 나누고
        아니면 짝수인 경우에만 나누기 2해서
        찾아감

        맨 뒷자리가 1이 아니고 홀수이면 
        못만드는 수

        오 훨씬 깔끔한듯?? ㅋㅋ
    '''

    a, b = map(int, input().split())
    r = 1

    while b != a:
        r += 1
        temp = b

        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2

        if temp == b:
            print(-1)
            break
    else:
        print(r)


from collections import deque
def secondSolu():

    '''
        다른 사람 풀이 2
        https://my-coding-notes.tistory.com/210

        위에 블로그에 BFS 풀이도 있길래 가져와봄

        DFS랑 똑같은 방식으로 하면 됨 ㅋㅋㅋ
    '''

    a, b = map(int, input().split())
    q = deque()
    q.append((a, 1))
    r = 1

    while q:
        n, t = q.popleft()
        if n > b:
            continue
        if n == b:
            print(t)
            break

        q.append((int(str(n) + '1'), t + 1))
        q.append((n * 2, t + 1))

    else:
        print(-1)