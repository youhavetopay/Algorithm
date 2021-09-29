import itertools

def checkPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True
        

def solution(numbers):
    answer = 0
    tempList = list(itertools.product(list(numbers), repeat=2))
    print(tempList)
    print(list(itertools.permutations(list(numbers))))
    return answer

n1 = '17'
n2 = '011'

print(solution(n1))
# print(solution(n2))