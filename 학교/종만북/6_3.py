# c = int(input())

# nList = []

# mList = []

# answers = []

# tempList = []
# for i in range(c):
#     nList.append(list(map(int, input().split(' '))))
#     mList.append(list(map(int, input().split(' '))))
    
    
#     for x in range(0, nList[i][1]*2, 2):
#         tempList.append(mList[i][x:x+2])

# print(tempList)

ans = 0
N , M = 0, 0
areFriends = [[False for _ in range(10)] for _ in range(10)]
havePair = [False for _ in range(10)]

def counting(n):
    global ans
    finished = True
    frist = -1
    for i in range(N):
        if not havePair[i]:
            finished = False
            frist = i
            break
    
    if finished:
        ans +=1
        
        return
    
    for j in range(frist+1, N):
        if (not havePair[frist]) and (not havePair[j]) and areFriends[frist][j]:
            havePair[frist] = True
            havePair[j] = True
            counting(n+1)
            havePair[frist] = False
            havePair[j] = False
    
    return

tc = int(input())

for t in range(1, tc+1):
    mList = []
    ans = 0
    
    areFriends = [[False for _ in range(10)] for _ in range(10)]
    havePair = [False for _ in range(10)]
    
    N, M = map(int, input().split())
    tempList = list(map(int, input().split()))
    for i in range(M):
        a = tempList[2*i]
        b = tempList[2*i+1]
        areFriends[a][b] = True
        areFriends[b][a] = True
    
    counting(0)

    print(ans)

    
