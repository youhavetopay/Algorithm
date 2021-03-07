n = int(input())

numbers = list(map(int, input().split()))

dp = [1] * n
dp2 = numbers[:]
maxValue = dp2[0]

for i in range(n):

    for j in range(i):

        if numbers[i] > numbers[j] and dp[i] < dp[j]+1:

            dp[i] = dp[j] +1 
            dp2[i] = max(dp2[i], dp2[j]+numbers[i])
        
        maxValue = max(maxValue, dp2[i])


print(maxValue)

# 이건 뭐야 ㅋㅋ
# n = int(input())
# a = list(map(int, input().split()))
# c = [0] * 1001
# for i in range(n): c[a[i]] = max(c[:a[i]]) + a[i]
# print(max(c))