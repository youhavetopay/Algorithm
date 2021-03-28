## 도시락 데우기

c = int(input())

hotTimes = list(map(int, input().split()))

eatTimes = list(map(int, input().split()))

totalTime = 0

checkList = [False] * c

print(max(hotTimes)+ sum(eatTimes))