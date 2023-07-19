
'''
    백준 1629. 곱셈

    A를 B번 곱한 수의 C로 나눈 나머지를 구하는 문제
'''

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def solution(a, b, c):

    '''
        나의 풀이 (못품)

        나의 접근법
        진짜 수학 너무 싫다 ㅋㅋ

        a,b,c 제한이 21억이라서 
        절때 그냥은 못 풀기 때문에
        고민좀 하다가
        문제 유형을 봤는데
        수학이랑 분할정복을 이용한 거듭제곱이라고 해서

        분할정복으로 해보려다가 포기..

        솔직히 2의 10억 승만 되더라도 100억자리가 넘는다고 함 ㅋㅋㅋㅋ
        이걸 어찌 풀어.... 
    '''

    dp = {}

    def divide_and_conq(now):

        if now in dp:
            return dp[now]
        
        if now == 0:
            return 1
        
        if now == 1:
            dp[now] = a
            return a

        if now % 2 != 0:
            dp[now] = divide_and_conq(now // 2) * divide_and_conq(now // 2) * divide_and_conq(1)
        else:
            dp[now] = divide_and_conq(now // 2) * divide_and_conq(now // 2)

        return dp[now]


    return divide_and_conq(b)


print(solution(A, B, C))



def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

        지수법칙이랑 나머지 분배 법칙?? 을 알아야 풀 수 있는 문제였음..
        핵심은 나머지 분배 법칙임
        (A X B) % C = (A % C) * (B % C) % C 이기 떄문에
        
        지수를 반으로 나누면서 분할 정복으로 풀어야 함..

        진짜 나머지 분배 법칙 모르면 절~~~~~~~~~~때 못풀 듯...
    '''

    a,b,c = map(int,sys.stdin.readline().split())

    def multi (a,n):
        if n == 1:
            return a%c
        else:
            tmp = multi(a,n//2)
            if n %2 ==0:
                return (tmp * tmp) % c
            else:
                return (tmp  * tmp * a) %c
            
    print(multi(a,b))