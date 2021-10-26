#체육복

def solution2(n, lost, reserve):
    answer = 0
    
    lost.sort()
    tempList = []
    for i in lost:
        if i in reserve:
            tempList.append(i)
    for i in tempList:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)

    count = 0
    for i in lost:
        
        if i-1 in reserve:
            reserve.remove(i-1)
            count += 1
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            count += 1
    
    answer = n - len(lost) + count

    return answer

# print(solution(4, [1,2,3,4], [1,2,3,4]))


#2021 10 26

def checkOverlap(lost, reserve):
    
    returnLost = []
    returnRe = []

    for num in lost:
        if num not in reserve:
            returnLost.append(num)
    
    for num in reserve:
        if num not in lost:
            returnRe.append(num)

    return returnLost, returnRe

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    lost, reserve = checkOverlap(lost, reserve)
    
    if lost == []:
        return n
    index = 0
    while index < len(reserve):

        if reserve[index] - 1 in lost:
            lost.remove(reserve[index] - 1)
            reserve.remove(reserve[index])
        elif reserve[index] + 1 in lost:
            lost.remove(reserve[index] + 1)
            reserve.remove(reserve[index])
        
        else:
            index += 1
        print(lost, reserve)

    
        

    answer = n - len(lost)
    
    return answer

print(solution(5, [5,3,1], [4,2,1]))
print(solution(5, [2,4], [3,5]))
print(solution(5, [4,2], [3,5]))