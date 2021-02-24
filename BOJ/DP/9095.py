count = int(input())

values = []

for i in range(count):
    values.append(int(input()))

dp = [0 for x in range(11)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for n in range(4, len(dp)):
    dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

for i in values:
    print(dp[i])


# t = int(input())
# arr = [1, 2, 4]
# for i in range(3, 10):
#     arr.append(arr[i - 3] + arr[i - 2] + arr[i - 1])
# for i in range(t):
#     n = int(input())
#     print(arr[n - 1])
