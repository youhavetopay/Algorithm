import sys
input = sys.stdin.readline

N = int(input())

dp = [0, 1]

for i in range(2, N+1):
    dp.append(i * dp[i-1])

answer = 0
N_str = str(dp[N])
N_length = len(N_str)

for i in range(N_length-1, -1, -1):
    if N_str[i] == '0':
        answer += 1
    else:
        break
if N == 0:
    print(0)
else:
    print(answer)