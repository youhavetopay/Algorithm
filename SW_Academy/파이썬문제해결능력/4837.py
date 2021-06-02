# 부분집합의 합

T = int(input())

def createSubset(arr, n, objectSum):
    answer = 0

    for i in range(1 << 12):
        sumValue = 0
        count = 0
        for j in range(12):
            if i & (1 << j):
                count += 1
                if count > n:
                    break
                sumValue += arr[j]
        if sumValue == objectSum and count == n:
            answer += 1

    return answer

arr = [x for x in range(1, 13)]
for test_case in range(1, T+1):
    numberLength, numberSum = map(int, input().split())

    print('#'+str(test_case), createSubset(arr, numberLength, numberSum))

