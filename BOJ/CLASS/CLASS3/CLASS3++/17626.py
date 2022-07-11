import sys
input = sys.stdin.readline

n = int(input())


now_n = n
dp = [0 for _ in range(n+1)]
dp[1] = 1

for i in range(2, n + 1):

    dp[i] = min([dp[i-(j*j)] for j in range(1, int(i**(1/2)+1))]) + 1

print(dp[n])
