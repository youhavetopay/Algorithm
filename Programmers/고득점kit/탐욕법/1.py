#체육복

def solution(n, lost, reserve):
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

print(solution(4, [1,2,3,4], [1,2,3,4]))