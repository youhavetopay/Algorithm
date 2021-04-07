def solution(n):
    tempList = ''
    while n> 0:
        result = n%3
        n = int(n/3)
        tempList += str(result)
    
    return int(tempList, 3)

number = int(input())

print(solution(number))