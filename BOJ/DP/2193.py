value = int(input())


dp = [-1 for x in range(91)]

dp[1] = 1
dp[2] = 1

for n in range(3, value+1):
    dp[n] = dp[n-1] + dp[n-2]

print(dp[value])

# 피보나치랑 같음