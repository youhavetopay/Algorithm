
'''
    백준 11660. 구간 합 구하기 5

    2차원 배열이 주어지고 좌표 두개가 주어지면
    해당 구간의 누적합을 출력하는 문제
'''

import sys
input = sys.stdin.readline

'''
    나의 풀이

    나의 접근법
    문제 제목에 다행이 구간 합이라고 되어 있어서
    누적합을 사용함

    0, 0 부터 n, n 까지 누적합을 만들고
    조건에 따라 분기처리 했음

    근데 파이썬으로 하면 시간초과뜨고 pypy3 으로 하면 통과는 하는데
    좀 어정쩡하게 푼거 같아서 좀 그럼.. ㅋㅋ
'''

def make_prefix_sum(nums):

    for y in range(len(nums)):
        if y > 0:
            nums[y][0] += nums[y-1][-1]
        for x in range(1, len(nums)):
            nums[y][x] += nums[y][x-1]

    return nums


N, M = map(int, input().split())

nums = [ list(map(int, input().split())) for _ in range(N)]

prefix = make_prefix_sum(nums)
for row in prefix:
    print(row)

for _ in range(M):

    y1, x1, y2, x2 = map(int, input().split())
    y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
    
    # 시작지점과 종료지점이 같은 곳
    if y2 == y1 and x2 == x1:
        
        # 0, 0 을 출력해야하는 경우
        if x2 == 0 and y2 == 0:
            print(prefix[0][0])
        
        # N 번째 행의 첫번째 열인 경우
        # 이전 행의 마지막을 빼주기
        elif x2 == 0:
            print(prefix[y2][x2] - prefix[y2-1][-1])
        
        # 그 외에는 바로 이전꺼를 빼주면 됨
        else:
            print(prefix[y2][x2] - prefix[y2][x2-1])

    # 처음부터 끝까지
    elif (y1 == 0 and x1 == 0) and (y2 == N-1 and x2 == N-1):
        print(prefix[y2][x2])
    else:
        answer = 0
        
        for y in range(y1, y2+1):

            if x2 == 0:
                if y == 0:
                    answer += prefix[0][0]
                else:
                    # 이전행의 마지막꺼
                    answer += (prefix[y][x2] - prefix[y-1][-1])
            else:
                if x1 == 0:
                    if y == 0:
                        answer += prefix[0][x2]
                    else:
                        # 이전행의 마지막꺼
                        answer += (prefix[y][x2] - prefix[y-1][-1])
                else:
                    answer += (prefix[y][x2] - prefix[y][x1-1])

        print(answer)



def firstSolu():

    '''
        다른 사람 풀이
        https://sodehdt-ldkt.tistory.com/76

        2차원 배열의 누적합을 사용해서 품

        i행 j열까지의 누적합 (0, 0 부터 i, j 까지의 사각형의 합)
        S(i, j) = S(i-1, j) + S(i, j-1) - S(i-1, j-1) + arr(i, j) 
        -> 왼쪽 + 위쪽 - 왼쪽상단대각선 + 현재 배열값
    
        그 후 포함되지 않는 부분을 빼주면 됨
        자세한 내용은 블로그에 있는 그림을 보기
    '''

    n, m = map(int, input().split())
    arr = []

    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)

    dp = [[0] * (n+1) for i in range(n+1)]

    # 누적합 계산
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]
    
    for row in dp:
        print(row)
    
    # 정답 출력
    for j in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
        print(result)
    

firstSolu()