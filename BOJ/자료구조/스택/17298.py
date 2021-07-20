# 오큰수 ㅋㅋ

numLen = int(input())

numList = list(map(int, input().split(' ')))

answer = [-1] * numLen
stack = [-1] * numLen
stack[0] = 0
top = 0
for i in range(1, numLen):
    if numList[i] > numList[stack[top]]:
        answer[stack[top]] = numList[i]
        

# 이건 시간초과
# for index, value in enumerate(numList):
#     rightIndex = -1
#     for checkIndex in range(index, numLen):
#         if value < numList[checkIndex]:
#             rightIndex = checkIndex
    
#     if rightIndex != -1:
#         answers[index] = numList[rightIndex]

# for i in answers:
#     print(i, end=' ')


