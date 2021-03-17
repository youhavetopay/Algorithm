import math

list1 = []
for i in range(5):
    list1.append(int(input()))

answer = 0
temp = 1

check = 0

for i in list1:
    temp *= i
    answer = math.sqrt(temp)
    
    if answer%(1) <= 0:
        check = 1

if check:
    print('found')
else:
    print('not found')



# 답 
# 파이썬에선 for esle 라는 구문이 가능함
# for에서 break가 생기지 않으면 else로 감

list2 = [int(input()) for _ in range(5)]

sumValue = 1

for i in list2:
    sumValue *= i

    if math.sqrt(sumValue) == int(math.sqrt(sumValue)):
        print('found')
        break

else:
    print('not found')