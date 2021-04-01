# 두수 뽑아서 더하기

def solution(numbers):
    answer = []
    
    length = len(numbers)
    
    for i in range(length):
        for j in range(i, length):
            if i==j:
                continue
            answer.append(numbers[i]+numbers[j])
    
    
    return sorted(set(answer))

number = [2,1,3,4,1]
number2 = [5,0,2,7]
print(solution(number2))