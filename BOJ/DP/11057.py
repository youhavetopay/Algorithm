value = int(input())

dp = [[0 for x in range(12)] for x in range(1001)]

dp[1] = [1,1,1,1,1,1,1,1,1,1,10]



for x in range(2, value+1, 1):
    sum_value = 0
    
    for j in range(1, 10, 1):
        temp_value = 0
        for z in range(1, j+1):
            temp_value += dp[x-1][z]
        dp[x][j] = dp[x-1][-1] - temp_value
       
        sum_value += dp[x][j]

    dp[x][-1] = sum_value

print(dp[value][-1]%10007)