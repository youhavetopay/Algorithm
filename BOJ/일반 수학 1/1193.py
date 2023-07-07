'''
    백준 1193. 분수찾기
    2차원 배열에서 일정한 규칙에 따라
    증가하고 줄어드는 분수가 있을 때
    숫자를 입력하면 X 번째 분수를 구하는 문제
'''

import sys
input = sys.stdin.readline

def solution(x):

    '''
        나의 풀이
        
        나의 접근법
        처음엔 증가하는 순서대로 구현했더니
        당연히 시간초과 (X의 최대값이 1천만 ㅋㅋ)

        그래서 이것도 결국 수열에 따른 규칙이 있으니까
        좀 더 고민해보니
        대각선으로 왔다갔다 하면서 분수가 생김
        대각선을 하나의 행으로 보면 짝수번째 행은 분모가 감소하고
        홀수번째 행은 분모가 증가하는 형태
        그리고 하나의 행의 길이는 1, 2, 3, 4, 5, ... 이런식으로 이전행의 길이 +1 으로 됨

        그래서 입력된 숫자가 몇번째 행인지 찾고 계산하는 방식으로 구현함 
    '''

    i = 1
    count = 0

    # 몇번째 행인지 찾기
    while i + count <= x:
        i += count
        count += 1
    
    # 해당 행의 시작 순번
    start = i

    # 짝수 행
    if count % 2 == 0:
        left = 1
        right = count
        for i in range(start, x):
            left += 1
            right -= 1
    
    # 홀수 행
    else:
        left = count
        right = 1
    
        for i in range(start, x):
            left -= 1
            right += 1
    
    return str(left) + '/' + str(right)

   

X = int(input())
print(solution(X))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(14))



def firstSolu():

    '''
        다른 사람 풀이
        https://deokkk9.tistory.com/11

        나랑 접근법이 똑같음
        입력받은 X이 몇번째 행의 몇번째 인지 찾고
        해당 행이 짝수인지 홀수인지 판별하고
        계산하는 방식

        식을 좀더 간단하게 표현해서 
        for문도 많이 없어서 훨씬 깔끔한듯??
    '''

    X = int(input())
    line = 1
    while X > line:
        X -= line
        line += 1
    
    if line % 2 == 0:
        a = X
        b = line - X + 1
    else:
        a = line - X + 1
        b = X
    
    print(a, '/', b, sep='')

