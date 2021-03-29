## 도시락 데우기
## 그리디 (탐욕)
c = int(input())

hotTimes = list(map(int, input().split()))

eatTimes = list(map(int, input().split()))
checkList = []
hotTotalTime = 0

maxValue = max(eatTimes)

while maxValue != -1:
    eatIndex = eatTimes.index(maxValue)
    hotTotalTime = hotTotalTime + hotTimes[eatIndex]
    checkList.append(hotTotalTime + eatTimes[eatIndex])
    hotTimes[eatIndex] = -1
    eatTimes[eatIndex] = -1
    maxValue = max(eatTimes)

print(max(checkList))