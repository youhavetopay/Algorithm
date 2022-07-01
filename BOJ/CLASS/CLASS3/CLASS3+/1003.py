T = int(input())

dp = [[1, 0], [0, 1], [1,1]]

while T > 0:

    N = int(input())
    dp_length = len(dp)
    if dp_length <= N:
        for i in range(dp_length, N+1):
            dp.append(
                [
                    dp[i-1][0] + dp[i-2][0], 
                    dp[i-1][1] + dp[i-2][1]
                ]
            )

    print(dp[N][0], dp[N][1])
    T -= 1