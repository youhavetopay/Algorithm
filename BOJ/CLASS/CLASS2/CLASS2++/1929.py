M, N = map(int, input().split(' '))

prime_number_list = [x for x in range(0, N+1)]

sqr_maxValue = int(N ** 0.5) + 1

for number in range(2, sqr_maxValue):
    for idx in range(number+number, N+1, number):
        prime_number_list[idx] = -1

for i in prime_number_list:
    if M <= i and i <= N and i != 1:
        print(i)