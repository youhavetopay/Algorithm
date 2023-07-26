
'''
    백준 9251. LCS
    최장 공통 부분수열의 길이를 구하는 문제
'''

import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

def solution(a, b):

    '''
        나의 풀이(못푼거나 마찬가지 ㅋㅋ)

        나의 접근법
        문자열이 최대 1000개라서
        완전탐색으로는 불가능 하다는 걸 알았음
        그렇게 고민하다가 알고리즘 분류를 봤는데
        DP 라고 하길래 더 놀랬음 ㅋㅋ

        그렇게 갈피 못잡고 있다가 결국 LCS 가 뭔지 검색해봤는데
        구하는 과정을 봤음
        일반적으로 LCS의 길이를 구하면 이렇게 구하는듯?
        LCS 구하는 방법 모르면 평생 못풀듯...
    '''

    max_length = max(len(a), len(b)) + 1

    dp = [ [0] * max_length for _ in range(max_length)]

    if len(a) < len(b):
        a, b = b, a
    
    for i, a_word in enumerate(a):
        i += 1
        for j, b_word in enumerate(b):
            j = j + 1
            if a_word == b_word:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return max(dp[-1])

print(solution(A, B))


def firstSolu():

    '''
        다른 사람 풀이
        https://myjamong.tistory.com/317

        단어가 일치하면 해당 위치 전에 누적된 값의 더하기 1
        해주면서 값을 계속 누적해나감

        위에 방법보다 훨씬 빠름.. ㄷㄷㄷ
    '''

    word1, word2 = input().strip(), input().strip()
    l1, l2 = len(word1), len(word2)

    cache = [0] * l2

    for i in range(l1):
        cnt = 0
        for j in range(l2):
            if cnt < cache[j]:
                cnt = cache[j]
            elif word1[i] == word2[j]:
                cache[j] = cnt + 1
    
    print(max(cache))