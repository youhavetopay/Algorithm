# 요세푸스 문제

# 원을 그리면서 K번째 숫자 빼는 문제
# pop으로 해도 되지만 그래도 직접 구현해봄

N, K = map(int, input().split(' '))

number_list = [str(x) for x in range(1, N+1)]

answers = []
loc = 0
count = 1
while len(answers) != N:
    
    while count < K:
        loc +=1
        if loc == N:
            loc = 0
        if number_list[loc] != 0:
            count += 1
            
        

    answers.append(number_list[loc])
    count = 0
    number_list[loc] = 0

print('<' + ', '.join(answers) + '>')