import sys
input = sys.stdin.readline

N, r, c = map(int, input().split(' '))

# r = y 0부터
# c = x 0부터
answer = 0

while N >= 0:

    N -= 1

    if 2 ** (N) > r and 2 ** (N) > c: # 1분면
        pass
    elif 2 ** (N) > r and 2 ** (N) <= c: # 2분면
        answer += (2**N) * (2**N) * 1
        c -= (2**N)
    elif 2 ** (N) <= r and 2 ** (N) > c: # 3분면
        answer += (2**N) * (2**N) * 2
        r -= (2**N)
    else:
        answer += (2**N) * (2**N) * 3
        r-= (2**N)
        c -= (2**N)


print(answer)