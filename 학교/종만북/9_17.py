n = int(input())

board = list(map(int, input().split()))
minValue = -987654321
dp = [[minValue for _ in range(n)] for _ in range(n)]
def play(left, rigth):

    if left > rigth:
        return 0
    

    ret = dp[left][rigth]

    if ret != minValue:
        return ret

    ret = max(
        board[left] - play(left + 1, rigth),
        board[rigth] - play(left, rigth-1)
    )

    if (rigth - left + 1) >= 2:
        ret = max(ret, -play(left+2, rigth))
        ret = max(ret, -play(left, rigth-2))

    dp[left][rigth] = ret

    return dp[left][rigth]
print(dp)
print(play(0, n-1))
