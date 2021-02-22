value = int(input())

dp = [0 for i in range(1001)]

dp[1] = 1
dp[2] = 3
for n in range(3, value+1):
    dp[n] = (dp[n-1] + (dp[n-2]*2))%10007

print(dp[value])


# n = int(input())
# a=1
# b=3
# for _ in range(n-1) : a,b = b,2*a+b
# print(a%10007)