
'''
    백준 9019. DSLR

    D, S, L, R 연산을 수행해서 목표 숫자를 만드는데
    최소 길이의 명령어를 출력하는 문제 
'''

import sys
from collections import deque
input = sys.stdin.readline

def solution(A, B):

    '''
        나의 풀이 (내가 풀었다고 할수 있나...? ㅋㅋ)

        나의 접근법
        각자의 연산을 전부 탐색하는 방식으로 해야할 것 같아서
        좀 생각해보니 BFS라는 결론이 나오게 됨 ㅋㅋ

        현재 숫자에서 각각의 연산을 하고 나온 결과값을 queue에 넣고
        다시 반복하는 방식으로 품
        근데 연산을 구현하는 과정이
        D, S 는 그냥 곱하고 빼는 연산인데
        L, R 연산이 한칸씩 회전시키는 연산이라서 그냥 deque에 담고 했는데
        pypy3으로도 시간초과 뜸..

        그래서 질문하기에서 정답코드를 어쩌다 봐버렸는데.. ㅋㅋㅋ
        L, R 연산을 수식으로 했길래 
        이게 어떻게 되는건지 확인해보니까 생각보다 간단했음... ㅋㅋ
        이거 수식으로 바꿔주니 통과함..

        근데 이거 시간제한이 엄~~~~~~청 빡빡해서 pypy3 으로 안하면 시간초과뜸..
        python으로 통과하려면 Bidirectional Search 를 통해서 양방향으로 접근해야 풀리는 듯 함..ㅋㅋ

        뭐 이런 문제가 다있어.. ㅡㅡ
    '''

    d = A
    target_num = B

    queue = deque()
    queue.append([d, ''])

    visited = set()
    visited.add(d)

    while queue:

        now_d, now_order = queue.popleft()
        if now_d == target_num:
            return now_order
        
        D = operate_D(now_d)
        if D not in visited:
            visited.add(D)
            queue.append([D, now_order + 'D'])

        S = operate_S(now_d)
        if S not in visited:
            visited.add(S)
            queue.append([S, now_order + 'S'])

        L = operate_L(now_d)
        if L not in visited:
            visited.add(L)
            queue.append([L, now_order + 'L'])

        R = operate_R(now_d)
        if R not in visited:
            visited.add(R)
            queue.append([R, now_order + 'R'])

    return ''


def operate_D(num):
    next_d_num = num * 2
    if next_d_num > 9999:
        next_d_num %= 10_000


    return next_d_num

def operate_S(num):
    next_d_num = num - 1
    if next_d_num < 0:
        next_d_num = 9999
    
    return next_d_num

def operate_L(num):

    num = (num // 1000) + (num % 1000 * 10)

    return num

def operate_R(num):

    num = (num % 10 * 1000) + (num // 10)

    return num

# T = int(input())

# for _ in range(T):
#     A, B = map(int, input().rstrip().split())
#     print(solution(A, B))

for _ in range(1):
    print(solution(1, 3333))
    print(solution(3333, 1))

def firstSolu():
    T = int(input())

    for _ in range(T):
        
        A, B = map(int,sys.stdin.readline().rstrip().split())

        visited = [False for i in range(10001)]
        deq = deque()
        deq.append([A,''])
        visited[A] = True

        while deq:
            num, command = deq.popleft()

            if num == B:
                print(command)
                break

            d = num * 2 % 10000
            if not visited[d]:
                visited[d] = True
                deq.append([d, command + 'D'])

            s = (num - 1) % 10000
            if not visited[s]:
                visited[s] = True
                deq.append([s, command + 'S'])

            l = num // 1000 + (num % 1000)*10
            if not visited[l]:
                visited[l] = True
                deq.append([l, command + 'L'])

            r = num // 10 + (num % 10) * 1000
            if not visited[r]:
                visited[r] = True
                deq.append([r, command + 'R'])


T = int(input())

for _ in range(T):
    
    '''
        다른 사람 풀이
        https://aia1235.tistory.com/27

        나랑 똑같은 풀이
        문제 풀었을때 고민하는 부분이 나랑 똑같음 ㅋㅋㅋ
        L, R 연산을 똑같이 deque로 하시다가 연산으로 바꿨다고 함 
    '''

    A, B = map(int,sys.stdin.readline().rstrip().split())

    visited = [False for i in range(10001)]
    deq = deque()
    deq.append([A,''])
    visited[A] = True

    while deq:
        num, command = deq.popleft()

        if num == B:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            deq.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            deq.append([s, command + 'S'])

        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            visited[l] = True
            deq.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            deq.append([r, command + 'R'])