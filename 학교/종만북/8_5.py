# c = int(input())

# answers = []

# for i in range(c):
#     n, m = map(int, input().split())

#     nList = list(map(int, input().split()))
#     mList = list(map(int, input().split()))

#     jlis = len(set(nList + mList))

#     answers.append(jlis)

# for i in answers:
#     print(i)

n, m = map(int, input().split())
nList = list(map(int, input().split()))
mList = list(map(int, input().split()))

dp = [0]

if nList[0] > mList[0]:
    dp[0] = mList[0]
else:
    dp[0] = nList[0]

