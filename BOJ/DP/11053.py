# value = int(input())

# answer = list(map(int, input().split(' ')))
# dp = [0 for i in range(value)]

# for i in range(value):
#     for j in range(i):
#         if answer[i] > answer[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i]+=1

# print(max(dp))    




n = int(input())

numbers = list(map(int, input().split()))

dp = [1] * n

for x in range(1, n):
    for y in range(x):
        if numbers[x] > numbers[y]:
            dp[x] = max(dp[x], dp[y]+1)

print(max(dp))
