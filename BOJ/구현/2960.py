# 에라토스테네스의 체

n, k = map(int, input().split())

numIndex = 0
numbers = [x for x in range(2, n+1)]
lenght = len(numbers)
count = 0

answer = 0

while count < k and numIndex < lenght:
    
    targetNum = numbers[numIndex]

    for i, v in enumerate(numbers):
        if v != -1 and v % targetNum == 0:
            answer = v
            numbers[i] = -1
            count += 1
            if count == k:
                break
    
    while numbers[numIndex] == -1:
        numIndex += 1
        if numIndex >= lenght:
            break
    
print(answer)
