
'''
    백준 2166. 다각형의 면적

    순서대로 점의 위치가 주어지면 해당 도형의 넓이를 구하는 문제
'''

import sys

input = sys.stdin.readline

def solution():

    '''
        나의 풀이

        사실상 내 풀이는 아님 ㅋㅋㅋ

        수학 모르면 절~~~~~~~~~~~~대 못푸는 문제

        xn, yn 이 있고 xn+1, yn+1 가 다음 연결된 위치라고 할때
        (xn+xn+1) * (yn-yn+1) 을 계속 해주면서 더해줌
        그 후 절대값의 1/2 이 너비가 됨 ㅋㅋ

        https://darkpgmr.tistory.com/86
        https://www.mathopenref.com/coordpolygonarea2.html
        이게 되는 원리는 여기 나와 있음...

        뭔소린지 모르겠으니 공식이나 외워야 할듯.. ㅋㅋㅋㅋ

    '''

    locs = []

    n = int(input())

    for _ in range(n):
        locs.append(list(map(int, input().split())))

    # n = 4

    # locs = [
    #     [0, 0],
    #     [0, 10],
    #     [10, 10],
    #     [10, 0]
    # ]


    total_sum = 0
    for i in range(n-1):
        total_sum += ((locs[i][0]+locs[i+1][0]) * (locs[i][1] -  locs[i+1][1]))
    
    total_sum += ((locs[-1][0]+locs[0][0]) * (locs[-1][1] -  locs[0][1]))
    total_sum = abs(total_sum)

    S = total_sum / 2

    print(round(S, 2))



    return


solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://my-coding-notes.tistory.com/258

        풀이 방식은 조금 다른데
        원리는 비슷한듯??
    '''

    x, y = [], []
    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    
    x.append(x[0])
    y.append(y[0])

    xr, yr = 0, 0
    for i in range(n):
        xr += x[i] * y[i+1]
        yr += y[i] * x[i+1]
    
    print(round(abs(xr-yr)/2, 1))