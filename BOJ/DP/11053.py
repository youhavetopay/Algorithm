value = int(input())

answer = list(map(int, input().split(' ')))
dp = [0 for i in range(value)]

for i in range(value):
    for j in range(i):
        if answer[i] > answer[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i]+=1

print(max(dp))    
