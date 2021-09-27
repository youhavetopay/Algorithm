# 부족한 금액 계산하기
def solution(price, money, count):
    answer = -1

    total = 0

    for i in range(1, count+1):
        total = (price * i) + total
    
    answer = money - total

    if answer >= 0:
        return 0
    else:
        return answer * -1
    
print(solution(100, 1, 4))