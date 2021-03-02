value = int(input())

wines = [0 for x in range(10003)]
dp = [0 for x in range(10003)]
answer = 0

for i in range(3, value+3):
    wines[i] = int(input())


for n in range(3, value+4):
    dp[n] = max(dp[n-3]+wines[n]+wines[n-1], dp[n-2]+wines[n])
    dp[n] = max(dp[n-1], dp[n])
    answer = max(answer, dp[n])

print(answer)


# 이거 이해 안감 나중에 확인하기 (index에러 뜸(리스트 길이 초과??))