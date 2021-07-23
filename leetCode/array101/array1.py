def findMaxConsecutiveOnes(nums) -> int:
    answer = 0
    tempAnswer = 0
        
    for i in nums:
        if i == 1:
            tempAnswer += 1
        else:
            if answer < tempAnswer:
                answer = tempAnswer
            tempAnswer = 0
            
    if answer < tempAnswer:
        answer = tempAnswer
    return answer

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))