N, M = map(int, input().split(' '))

numbers = list(map(int, input().split(' ')))

answer = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for z in range(j+1, N):
            sum_value = numbers[i] + numbers[j] + numbers[z]
            
            if answer < sum_value <= M:
                answer = sum_value

print(answer)