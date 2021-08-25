# 숨바꼭질

from collections import deque

N, K = map(int, input().split())

tempList = []

if N >= 1:
    tempList.append(N-1)
tempList.append(N+1)
tempList.append(N*2)

checkDic = {}

queue = deque()
queue.append(tempList)

nowLoc = N
count = 0
while nowLoc != K:

    moveList = queue.popleft()
    tempList = []

    for next in moveList:

        nowLoc = next

        if nowLoc == K:
            break

        if next - 1 >= 0:
            try:
                checkDic[next-1] += 1
            except:
                tempList.append(next-1)
                checkDic[next-1] = 0
        
        try:
            checkDic[next+1] += 1
        except:
            tempList.append(next+1)
            checkDic[next+1] = 0
        
        if next*2 <= 100000:
            try:
                checkDic[next*2] += 1
            except:
                tempList.append(next*2)
                checkDic[next*2] = 0

    queue.append(tempList)
    count += 1

print(count)