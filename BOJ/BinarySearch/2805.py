# 나무자르기 2805
treeCount, needTree = map(int, input().split())
treeHeights = list(map(int, input().split()))
maxValue = 2000000000
minValue = 0
mid = round((maxValue + minValue) / 2) 
preMid = mid
preSum = 0
while True:

    sumValue = sum([i-mid if mid < i else 0 for i in treeHeights])
    # 이게 그냥 for문으로 하는것 보다 빠름?

    if sumValue == needTree:
        answer = mid
        break
    if sumValue < needTree:
        maxValue = mid
    elif sumValue > needTree:
        minValue = mid
    
    mid = round((maxValue + minValue) / 2)
    if preMid == mid:
        if sumValue < needTree:
            answer = mid -1
            break    
        answer = mid
        break
    preSum = sumValue
    preMid = mid
print(answer)