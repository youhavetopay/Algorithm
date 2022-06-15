# 검증수

# 그냥 입력받아서 제곱수 더하고 나누기 10의 나머지

numbers = list(map(int, input().split(' ')))

answer = 0

for number in numbers:
    answer += number**2

print(answer%10)