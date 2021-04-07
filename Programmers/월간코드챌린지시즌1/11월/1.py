# 내적 구하기

def solution(a,b):
    answer = 0

    for i, j in zip(a,b):
        answer += i*j
    
    return answer