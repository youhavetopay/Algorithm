# value = int(input())

# dp = [[0 for i in range(12)] for j in range(2)]

# div_value = 1000000000

# for i in range(2, 11):
#     dp[1][i] = 1

# answer = 9

# for i in range(2, value+1):
#     answer = 0
#     for j in range(1, 11):
#         dp[i%2][j] = dp[(i-1)%2][j-1] + dp[(i-1)%2][j+1] %div_value
#         answer = (answer+dp[i%2][j])%div_value
# print(answer)

# 슬라이딩 윈도우?? 기법 (공간복잡도 줄이는 방법)


value = int(input())

dp = [[0 for i in range(10)] for j in range(101)]

div_value = 1000000000


for i in range(10):
    dp[1][i] = 1

for i in range(2, value+1):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i-1][1] %div_value
        elif j == 9:
            dp[i][j] = dp[i-1][8] % div_value
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % div_value

answer = 0

for i in range(1, 10):
    answer = (answer+dp[value][i]) % div_value

print(answer%div_value)