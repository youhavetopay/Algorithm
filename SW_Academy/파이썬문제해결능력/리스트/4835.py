# 구간합

def findAnswer(array, length ,width):
    
    maxValue = float('-inf')
    minValue = float('inf')

    for i in range(length - width + 1):
        sumValue = 0

        for j in range(width):
            sumValue += array[i+j]
        
        if sumValue < minValue:
            minValue = sumValue

        if sumValue > maxValue:
            maxValue = sumValue
    

    return maxValue - minValue

T = int(input())

for test_case in range(1, T+1):

    arrayLength, width = map(int, input().split())

    array = list(map(int, input().split()))

   
    print('#'+str(test_case), findAnswer(array, arrayLength, width))