# 이항계수 구하기

# N ! / ( K! * (N-K)! )

N, K = map(int, input().split(' '))

n = 1
for i in range(1, N+1):
    n *= i

k = 1
for i in range(1, K+1):
    k *= i

r = 1
for i in range(1, N - K+1):
    r *= i

print(int(n/(r*k)))