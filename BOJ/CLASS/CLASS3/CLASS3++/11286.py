
'''
    백준 11286. 절댓값 힙

    절댓값을 기준으로 힙에 넣고
    뺼때는 절대값이 같은 게 여러개라면
    그 중 가장 낮은 수를 빼는 문제
'''

import sys, heapq
input = sys.stdin.readline

'''
    나의 풀이
    
    나의 접근법
    파이썬의 heapq 모듈을 사용함

    push할때는 절댓값과 x를 같이 넣었고

    pop할때는 
    절댓값이 같은 얘들을 전부 빼서
    다른 heap에 넣고 최소값을 출력한 다음
    다른 heap에 넣었던 값을 다시 원래 heap에다 push해줌

    heap을 라이브러리 없이 구현했다면 좀 힘들었을듯??
    heap에 대해 잘 안다면 쉽게 쉽게 풀 수 있을 듯 함
'''

def push(heap, x):
    heapq.heappush(heap, (abs(x), x))
    return

def pop(heap):

    if not heap:
        return 0

    min_abs = heap[0][0]

    temp_heap = []

    while heap and min_abs == heap[0][0]:
        heapq.heappush(temp_heap, heapq.heappop(heap)[1])

    min_num = heapq.heappop(temp_heap)

    while temp_heap:
        heapq.heappush(heap, (min_abs, heapq.heappop(temp_heap)))

    return min_num

N = int(input())

heap = []


for i in range(N):
    x = int(input())

    if x == 0:
        print(pop(heap))
    else:
        push(heap, x)


def firstSolu():

    '''
        다른 사람 풀이
        https://hongcoding.tistory.com/77

        엥? 그냥 절댓값을 기준으로 넣고
        빼줘도 상관없나봄 ㅋㅋ
        알아서 최소값인걸 찾나봄 ㅋㅋ
    '''

    n = int(input())
    q = []

    for i in range(n):
        a = int(sys.stdin.readline().rstrip())
        if a != 0:
            heapq.heappush(q, (abs(a), a))
        else:
            if not q:
                print(0)
            else:
                print(heapq.heappop(q)[1])