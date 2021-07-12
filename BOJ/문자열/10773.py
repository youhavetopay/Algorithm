# 제로

count = input()

answer = []
for i in range(int(count)):
    number = int(input())
    if number == 0 and answer != []:
        answer.pop()
    else:
        answer.append(number)

print(sum(answer))