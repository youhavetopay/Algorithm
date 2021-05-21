# 수 정렬하기 2

import sys

# 왜 시간초과지? ㅋㅋ 합병정렬
def mergeSort(first, second, f_len, s_len):
    
    if f_len > 1:
        if f_len % 2 == 0:
            first = mergeSort(first[:f_len//2], first[f_len//2:], f_len//2, f_len//2)
        else:
            first = mergeSort(first[:f_len//2], first[f_len//2:], f_len//2, f_len//2+1)
    if s_len > 1:
        if s_len % 2 == 0:
            second = mergeSort(second[:s_len//2], second[s_len//2:], s_len//2, s_len//2)
        else:
            second = mergeSort(second[:s_len//2], second[s_len//2:], s_len//2, s_len//2+1)
        
    
    returnList = []

    while first != [] or second != []:
        if first == []:
            for i in second:
                returnList.append(i)
            
            return returnList
    
        if second == []:
            for i in first:
                returnList.append(i)
            
            return returnList

        if first[0] > second[0]:
            returnList.append(second.pop(0))
        else:
            returnList.append(first.pop(0))
    
    return returnList

N = int(sys.stdin.readline())

list1 = []

for i in range(N):
    list1.append(int(sys.stdin.readline()))

if N % 2 == 0:
    list1 = mergeSort(list1[:N//2], list1[N//2:], N//2, N//2)
else:
    list1 = mergeSort(list1[:N//2], list1[N//2:], N//2, N//2+1)

for i in list1:
    print(i)