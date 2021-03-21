dp = []

minvalue = float('-inf')

def solve(indA, indB):
    if N <= indA or M <=indB:
        return -1
    ret = dp[indA + 1][indB + 1];

    if ret != -1:
        return ret

    ret = 0

    a = nList[indA]
    b = mList[indB]

    if indA == -1:
        a = minvalue
    if indB == -1:
        b = minvalue

    maxNum = max(a,b)

    for i in range(indA+1,N):
        if maxNum >= nList[i] : continue

        ret = max(ret, solve(i, indB)+1)
    
    for i in range(indB+1,M):
        if maxNum >= mList[i] : continue

        ret = max(ret, solve(indA, i)+1)
    
    dp[indA + 1][indB + 1] = ret
    return dp[indA + 1][indB + 1]


c = int(input())

answers = []

for x in range(c):
    N, M = map(int, input().split())

    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))


    dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]

    answers.append(solve(-1, -1))

for i in answers:
    print(i)
print(dp)