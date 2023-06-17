def solution(arrayA, arrayB):

    '''
        나의 풀이(내가 푼건 아님 ㅋ)
        자연수로 이루어진 리스트 두개가 있을 때
        한쪽 리스트의 공약수이면서 다른쪽에선 모든 수를 나눌 수 없는 수를 
        만족하는 최대의 수를 구하는 문제

        나의 접근법
        처음엔 모든 약수들을 구해서 set의 교집합으로 구해볼려고 했으나
        당연히 시간초과
        그래서 다시 생각해봤는데
        두 리스트의 최소값들 중 최대값이 정답의 범위의 최대이고
        2가 최소 이기 때문에
        반복문으로 해봤는데 이것도 시간초과....
        결국 질문하기로 봤는데
        양쪽 리스트의 최대 공약수를 구해서 비교하면 된다고 함..
        그래서 유클리드 호제법으로 리스트의 최대 공약수를 구한 뒤 비교해서 품

        이런 수학문제 너무 어려운듯..
        유클리드 호제법을 잘 사용해보지 못해서
        더 그런듯..
    '''
    
    a_GCD = arrayA[0]
    b_GCD = arrayB[0]

    for i in range(1, len(arrayA)):
        a_GCD = GCD(a_GCD, arrayA[i])
    
    for i in range(1, len(arrayB)):
        b_GCD = GCD(b_GCD, arrayB[i])

    flags = [True, True]
    
    for num in arrayB:
        if num % a_GCD == 0:
            flags[0] = False
            break
    
    for num in arrayA:
        if num % b_GCD == 0:
            flags[1] = False
            break

    if flags == [True, True]:
        return max(a_GCD, b_GCD)
    
    elif flags == [False, True]:
        return b_GCD
    elif flags == [True, False]:
        return a_GCD
    else:
        return 0

def GCD(a, b):

    if b == 0:
        return a
    
    return GCD(b, a%b)



from math import gcd
from functools import reduce

def firstSolu(arrayA, arrayB):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/135807/solution_groups?language=python3

        나랑 똑같은 풀이인데
        reduce랑 gcd 라이브러리를 사용해서 훨씬 더 깔끔하게 풀어냄

    '''

    gcd1, gcd2 = reduce(gcd, arrayA), reduce(gcd, arrayB)
    answer = []
    if all(each % gcd2 for each in arrayA):
        answer.append(gcd2)
    if all(each % gcd1 for each in arrayB):
        answer.append(gcd1)
    return max(answer) if answer else 0