def solution(n):
    answer = 1
    
    min_num = 1
    max_num = 1
    
    while min_num < n:
        
        

        sum_num = min_num
        max_num = min_num + 1
        
        while sum_num < n:
            sum_num += max_num
            max_num += 1
        
        if sum_num == n:
            print(min_num, max_num)
            answer += 1
            
        min_num += 1
            
    
    return answer


print(solution(15))