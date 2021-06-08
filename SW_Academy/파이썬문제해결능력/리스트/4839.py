# 이진탐색

T = int(input())

def binarySearch(start, end, findValue):
    
    count = 1
    while start <= end:
        mid = (start + end) // 2
        
        if mid == findValue:
            return count
        elif mid < findValue:
            start = mid
        else:
            end = mid

        count += 1

for test_case in range(1, T+1):
    totalPage, aFindPage, bFindPage = map(int, input().split())

    aCount = binarySearch(1, totalPage, aFindPage)
    bCount = binarySearch(1, totalPage, bFindPage)
    
    if aCount < bCount:
        print('#'+str(test_case), 'A')
    elif aCount > bCount:
        print('#'+str(test_case), 'B')
    else:
        print('#'+str(test_case), '0')

