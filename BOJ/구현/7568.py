# 덩치

n = int(input())

total = [[]] * n

for i in range(n):
    total[i] = list(map(int, input().split()))

answers = [-1] * n


for i, v in enumerate(total):
    
    count = 0

    for j, val in enumerate(total):
        if v[0] < val[0] and v[1] < val[1]:
            count += 1

    answers[i] = count + 1

for value in answers:
    print(value, end=' ')
