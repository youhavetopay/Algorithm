
'''
    백준 9935. 문자열 폭발
    특정 문자열이 없어질때까지 반복해서 남은 문자열을 출력하는 문제
'''


import sys
input = sys.stdin.readline

def solution():

    '''
        나의 풀이

        나의 접근법
        비슷한 문제를 풀어본 것 같아서 스택으로 하면 될 것 같은 생각이 들었음
        그래서 스택에 문자를 담고
        스택의 크기가 폭발 문자열 길이 이상일 경우 해당 크기 만큼 잘라서 비교한 후
        같으면 빼주는 방식으로 했음

    '''

    S = input().rstrip()

    bomb_s = list(input().rstrip())

    stack = []

    for word in S:

        stack.append(word)

        if len(stack) >= len(bomb_s):
            if stack[len(stack) - len(bomb_s):] == bomb_s:
                i = 0
                while i < len(bomb_s):
                    stack.pop()
                    i += 1
    

    if len(stack) == 0:
        print('FRULA')
    else:
        print(''.join(stack))

solution()

def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@heejun32/%EB%B0%B1%EC%A4%80-9935%EB%B2%88-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AD%EB%B0%9C-Python

        나랑 똑같이 스택을 활용해서 푸심

        코드는 거의 똑같은데
        스택 슬라이싱 하는 부분에서 -ex_len 해준게 디게 좋은듯!!

        나는 - 해주면 뒤집어지는줄 알고 착각하고 있었음 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ

        전체적으로 나보다 좀 더 깔끔한 풀이인듯 함 !
    
    '''

    S = input().rstrip()
    explosion_string = input().rstrip()

    stack = []
    ex_len = len(explosion_string)

    for i in range(len(S)):
        stack.append(S[i])

        if ''.join(stack[-ex_len:]) == explosion_string:
            for _ in range(ex_len):
                stack.pop()
    
    if stack:
        print(''.join(stack))
    else:
        print('FRULA')