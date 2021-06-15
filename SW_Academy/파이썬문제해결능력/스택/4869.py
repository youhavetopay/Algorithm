T = int(input())
# 동적 계획법
# 타일 채우기
for test_case in range(1, T+1):
    N = int(input())

    dp = [0] * 31

    dp[1] = 1
    dp[2] = 3

    for i in range(3, N//10+1):
        dp[i] = dp[i-1] + (dp[i-2] * 2)
    
    print('#'+str(test_case), dp[N//10])

