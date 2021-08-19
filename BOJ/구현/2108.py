# 통계학
import sys


n = int(sys.stdin.readline())

numbers = [0] * n
sumValue = 0

dic = {}

maxValue = -999999
minValue = 99999
for i in range(n):
    numbers[i] = int(sys.stdin.readline())
    sumValue += numbers[i]

    try:
        dic[numbers[i]] += 1
    
    except:
        dic[numbers[i]] = 1

    if maxValue < numbers[i]:
        maxValue = numbers[i]
    
    if minValue > numbers[i]:
        minValue = numbers[i]
# print()
# 평균
print(round(sumValue/n))

# 중앙값
sortedNumbers = sorted(numbers)
print(sortedNumbers[n//2])

maxShowValue = -1
maxShowKey = -1

checkList = []

for k, v in dic.items():
    if maxShowValue < v:
        maxShowKey = k
        maxShowValue = v
        checkList = []
        checkList.append(k)
    elif maxShowValue == v:
        checkList.append(k)

# 최빈값
if len(checkList) > 1:
    print(sorted(checkList)[1])
else:
    print(maxShowKey)

# 범위
print(maxValue-minValue)