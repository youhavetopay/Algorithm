# 특별한 정렬

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    inputList = list(map(int, input().split()))

    flag = 0

    for i in range(10):
        if (i+1) % 2 == 0:
            flag = 1
        else:
            flag = 0
        valueIndex = i
        for j in range(i+1, N):
            if flag == 1:
                if inputList[valueIndex] > inputList[j]:
                    valueIndex = j
            else:
                if inputList[valueIndex] < inputList[j]:
                    valueIndex = j
        inputList[i], inputList[valueIndex] = inputList[valueIndex], inputList[i]

    print('#'+str(test_case), end=" ")
    for i in range(10):
        print(inputList[i], end=" ")
    print()