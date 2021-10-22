# 연속 수열의 합 구하기
def birthday(n,s, d, m):
    # Write your code here
    
    answer = 0
    
    if n == m:
        if sum(s) == d:
            return 1
        else:
            return 0
    
    for i in range(n-m+1):
        sumValue = 0
        for j in range(i, i+m):
            sumValue += s[j]
        
        if sumValue == d:
            answer +=1
    
    return answer


print(birthday(19, [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7))