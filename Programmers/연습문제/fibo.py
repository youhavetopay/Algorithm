def solution(n):
    fibo_list = [0,1,1]
    
    now_length = 2
    
    if n > now_length:
        while now_length <= n:
            fibo_list.append((fibo_list[now_length - 1] + fibo_list[now_length]) % 1234567)
            print(fibo_list)
            now_length += 1
    
    return fibo_list[n]

print(solution(3))