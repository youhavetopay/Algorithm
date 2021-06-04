
N, S = map(int, input().split())

array = list(map(int, input().split()))

answer = 0

for i in range(1, 1 << N):
    sumValue = 0
    for j in range(N):
        if i & (1 << j):
            sumValue += array[j]
    
    if sumValue == S:
        answer += 1

print(answer)