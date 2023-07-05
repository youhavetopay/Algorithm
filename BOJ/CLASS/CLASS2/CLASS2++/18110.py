'''
    백준 18110. solved.ac

    나의 풀이
    숫자들이 주어지면 절사평균 30%을 구하는 문제
    절사평균 30%은 상위 15% 하위 15%를 제외하고 평균을 구하는 것임

    나의 접근법
    일단 입력 받을 수를 오름차순으로 정렬한 후
    절사평균을 구하는 방식으로 함
    소수점 자리는 반올림 하라고 해서 파이썬의 round를 사용했는데 실패라고 함 ㅋㅋ
    게시판에서 반례를 찾아보니 12.5 를 반올림하면 13이 되야 한다고 함 ㅋㅋ
    파이썬에서는 12.5는 12이 되서 내가 round함수를 구현함 -> 확인해보니 5인경우는 앞자리가 짝수면 버리고 홀수면 올린다고 함 ㅋㅋ
    그랬더니 풀림 ㅋㅋ

    이 문제를 마지막으로 class 2 다 땀 ㅋㅋ
    
'''


import sys
input = sys.stdin.readline

def my_round(num):

    if num % 1 >= 0.5:
        return int(num) + 1
    
    return int(num)

def mySolu():
    N = int(input())

    difficulty = []

    for _ in range(N):
        difficulty.append(int(input()))


    difficulty.sort()
    if N == 0:
        print(0)
    else:
        trimmed_mean = my_round((N * 0.3) * 0.5)
        start = trimmed_mean
        end = len(difficulty) - trimmed_mean

        total = difficulty[start:end]
        print(my_round(sum(total) / len(total)))




def firstSolu():

    '''
        다른 사람 풀이
        https://ywtechit.tistory.com/210

        나랑 똑같은 풀이법
        심지어 나랑 겪었던 똑같은 문제를 겪었음 (python round)
        이렇게 반올림하는 걸 사사오입 반올림 이라고 함 ㅋㅋ
    '''

    def round2(num):
        return int(num) + (1 if num - int(num) >= 0.5 else 0)
 
    n = int(input())
    if not n:
        print(0)
    else:
        score = [int(input()) for _ in range(n)]
        trunc = round2(n * 0.15)
        apply_trunc = sorted(score)[trunc: n - trunc]
        average = round2(sum(apply_trunc) / len(apply_trunc))
        print(average)