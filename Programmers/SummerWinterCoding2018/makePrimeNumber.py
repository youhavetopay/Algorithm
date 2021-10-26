def selectNumber(nums, selectCount, sumValue, nowIndex):
    
    answer = 0

    if nowIndex >= len(nums):
        if selectCount != 3:
            return 0
        else:
            answer = checkPrime(sumValue)
            return answer

    if selectCount == 3:
        answer = checkPrime(sumValue)
        return answer
    

    a = selectNumber(nums, selectCount + 1, sumValue+nums[nowIndex], nowIndex + 1)
    b = selectNumber(nums, selectCount, sumValue, nowIndex +1)

    answer += (a+b)

    return answer

def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def solution(nums):
    answer = -1
    
    answer = selectNumber(nums, 0, 0, 0)

    return answer

n1= [1,2,3,4]
n2 = [1,2,7,6,4]

print(solution(n2))