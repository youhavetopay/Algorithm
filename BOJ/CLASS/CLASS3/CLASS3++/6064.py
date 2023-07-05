
'''
    백준 6064. 카잉 달력

    규칙에 따라 정해지는 년도가 있을 때
    입력되는 x, y 가 몇번째 년도인지 계산하는 문제
'''

import sys
input = sys.stdin.readline

def solution(M, N, x, y):

    '''
        나의 풀이

        나의 접근법
        처음엔 그냥 무식하게 1번부터 ~ 마지막 년도까지 전부 계산한다음 했는데
        당연히 시간초과 ㅋㅋ
        딱 봐도 년도가 만들어지는 규칙이 있어서 좀 살펴보니
        숫자가 반복되는 걸 확인했고
        일정한 규칙에 따라 만들어지는 걸 확인함
        1 ~ min(M, N) 번 까지는 1,1  2,2, 3,3 .... 이렇게 이뤄지고
        
        min(M, N) 부터는 
        만약 M < N 인 경우 x, (M + x) % M -> (이게 x + M 번째) 대충 이런식이고
        이 다음 x가 다시 나올때(x + 2M 번째)는 x, (이전 y - (N - M)) 이런식으로 반복됨

        이 규칙을 발견해서
        M < N, M > M 이렇게 두가지 경우로 나눠서
        해당 x 혹은 y 일때의 년도를 모두 구하고 체크하는 방식으로 품
        
        실행속도가 빠른 건 아니라서
        엄~~~청 오래 걸리긴 하지만 어찌됐든 통과는 함 ㅋㅋㅋ (4000ms ㅋㅋㅋㅋ)
        결과 기다리는데 엄청 긴장했음 ㅋㅋㅋ
        아마 수열의 규칙이 있기 때문에
        수학적 사고?? 가 뛰어나면 훨씬 효율적으로 풀 수 있을듯??
        근데 난 이게 한계 ㅋㅋ
    '''

    if x == y:
        return x

    if M < N:
        i = 0
        now_x, now_y = x, calculate(M + x, N)
        count = M + x
        years = set()

        if now_y == y:
            return count

        while (now_x, now_y) not in years:
            years.add((now_x, now_y))

            if now_y == y:
                return count

            if now_y <= (N - M):
                now_y = N + (now_y - (N - M))
            else:
                now_y = now_y - (N - M)

            count += M
            i += 1
            


    elif M > N:
        i = 0
        now_x, now_y = calculate(N + y, M), y 
        count = N + y
        years = set()

        if now_x == x:
            return count

        while (now_x, now_y) not in years:
            years.add((now_x, now_y))

            if now_x == x:
                return count

            if now_x <= (M - N):
                now_x = M + (now_x - (M - N))
            else:
                now_x = now_x - (M - N)

            count += N
            i += 1
        

    return -1

def calculate(num, target):

    if num % target == 0:
        return target
    
    return num % target

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solution(M, N, x, y))


def firstSolu(M, N, x, y):

    '''
        다른 사람 풀이
        https://aia1235.tistory.com/37

        역시나.. 
        훨씬 간단하게 풀 수 있는 문제였음 ㅋㅋ

        정답을 K 라고 했을 때
        K = (M * p + x) = (N * q + y) 를 만족한다고 함
        이 식을 조금 변형하면
        (K - x)는 M으로 나눠 떨어지고 (K - y) 는 M 으로 나눠진다고 함

        그래서 저 조건을 코드로 나타내고
        K를 증가시키면서 저 조건에 맞으면 정답이라고 함

        근데 K를 1씩 증가시키면 당연히 시간초과이기 때문에
        K = (M * p + x) 이므로
        초기값을 x로 해놓고 M 씩 증가시키면 됨

        라고 하는데 뭔소리인지 모르겠음 ㅋㅋㅋㅋㅋ
        그래도 성능은 확실한듯 약 1900ms ㄷㄷ
        내꺼보다 2배 빠름 ㅋㅋ
    '''

    K = x

    while K <= M * N:
        if (K - x) % M == 0 and (K - y) % N == 0:
            return K
        K += M
    return -1