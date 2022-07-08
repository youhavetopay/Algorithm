import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 501

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

while T > 0:

    N = int(input())

    for i in range(5, N+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[N])
    T -= 1

