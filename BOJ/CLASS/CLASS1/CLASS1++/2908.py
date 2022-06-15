# 숫자입력받아서 뒤집은 다음 가장 큰 수 출력

numbers = list(map(str, input().split(' ')))

max_number = -1
for number in numbers:
    if max_number <= int(number[::-1]):
        max_number = int(number[::-1])

print(max_number)