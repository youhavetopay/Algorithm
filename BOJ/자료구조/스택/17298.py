# 오큰수 ㅋㅋ

numLen = int(input())

numList = list(map(int, input().split(' ')))

answers = [-1] * numLen
answers[-1] = -1

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


