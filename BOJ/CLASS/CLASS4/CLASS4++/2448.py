
'''
    백준 2448. 별 찍기 - 11
    규칙에 따른 별을 출력하는 문제
'''

import sys
input = sys.stdin.readline

from collections import deque
import math

def solution():

    '''
        나의 풀이

        나의 접근법
        이런 별찍기 문제는 일정 패턴이 반복되기 때문에
        
        분할정복이라고 생각했음

        그래서 일단 이게 몇번째 삼각형인지 계산하기 위해
        로그로 계산을 함(입력값은 3 x 2^n 으로 만 주어짐)

        그렇게 삼각형을 살펴보니
        이전에 만들었던 삼각형을 위에 붙이고 옆으로 붙이는 방식이였음
        그리고 삼각형 사이에 공백이 있는데 삼각형 제일 바깥쪽 오른쪽에도 공백을 출력하면 안되나 궁금했는데
        예제 케이스를 드래그 해보니 공백이 있길래 안심하고 걍 넣어줌 ㅋㅋㅋ

        위에다 넣을려면 배열 앞칸에다 넣어야 하는데
        그러기 위해서 deque를 사용함 
        -> 솔직히 삼각형 뒤집어서 넣으면 deque 안써도 될 것 같은데 귀찮아서 그냥 deque 씀 ㅋㅋㅋ

        그렇게 반복문으로 붙여주고 넣어주고를 반복해서 삼각형을 만들어줌


    '''

    N = int(input())

    # 이전에 만들었던 삼각형들
    base = [
        [
            '  *  ',
            ' * * ',
            '*****'
        ]
    ]

    # 출력용 삼각형
    answer = deque([
        '  *  ',
        ' * * ',
        '*****'
    ])

    i = 0
    # 몇 번째 삼각형인지 구하기
    max_length = math.log2((N // 3))

    while i < max_length:

        # 옆에 붙이기
        for idx, row in enumerate(answer):
            answer[idx] += ' ' + row

        # 위에 넣어주려면 row의 길이를 맞춰줘야 함
        now_row_length = len(answer[0])
        empty_length = (now_row_length - len(base[-1][0])) // 2

        # 마지막에 만들었던 삼각형을 뒤에서 부터 넣어주기
        for j in range(len(base[-1])-1, -1, -1):
            answer.appendleft(
                (' ' * empty_length) + base[-1][j] +  (' ' * empty_length)
                )
            
        # 지금 만든 삼각형 base 에 넣어주기
        base.append(list(answer))


        i += 1

    for row in answer:
        print(row)

solution()

def firstSolu():

    '''
        다른 사람 풀이
        https://hongcoding.tistory.com/90

        처음에 그래프?의 빈칸을 전부 만들어 둠 -> N x 2 가 너비
        그 후 베이스가 되는 기본 삼각형을 위치에 따라 반복해서 넣어줌

        가장 재귀스럽게 풀어낸듯 한 풀이 였음 ㅎㅎ

    '''

    n = int(input())

    # 빈칸 만들어 주기
    graph = [[''] * 2 * n for _ in range(n)]

    def recursive(x, y, N):

        # N 이 3 이면 기본 삼각형 만들어 주기
        if N == 3:
            graph[x][y] = '*'
            graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'

            for i in range(-2, 3):
                graph[x+2][y+i] = '*'
        else:
            # 아니라면 N이 3이 될때까지 나누기 
            nextN = N // 2
            recursive(x, y, nextN)
            recursive(x + nextN, y - nextN, nextN)
            recursive(x - nextN, y + nextN, nextN)
    
    recursive(0, n-1, n)

    for i in graph:
        print(''.join(i))