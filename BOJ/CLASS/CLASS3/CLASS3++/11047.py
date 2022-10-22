import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))

coin_list = []

total_coin_count = 0
for _ in range(N):
    coin_list.append(int(input()))

now_money = K
for i in range(N-1, -1, -1):
    if coin_list[i] <= now_money:
        total_coin_count += now_money // coin_list[i]
        now_money = now_money % coin_list[i]

    if now_money <= 0:
        break

print(total_coin_count)
