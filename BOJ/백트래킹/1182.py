
N, S = map(int, input().split())

array = list(map(int, input().split()))

answer = 0


# 이거 잘 기억하기
# 모든 부분 수열 만들어주는 거임
for i in range(1, 1 << N):
    sumValue = 0
    for j in range(N):
        if i & (1 << j):
            sumValue += array[j]
    
    if sumValue == S:
        answer += 1

print(answer)