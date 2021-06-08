# 최대 최소 차이 구하기

import sys

def findMinMax(arr):
    minValue = 1000000
    maxValue = 0

    for number in arr:
        if number > maxValue:
            maxValue = number
        if number < minValue:
            minValue = number
    
    return maxValue - minValue


input = sys.stdin.readline

testCount = int(input().strip())


for test_case in range(1, testCount + 1):
    arrayCount = int(input().strip())
    array = list(map(int, input().strip().split()))
    answer = findMinMax(array)

    print('#'+str(test_case), answer)
