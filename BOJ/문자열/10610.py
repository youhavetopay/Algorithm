# 30

numberStr = input()

if '0' not in numberStr:
    print(-1)
else:
    answer = ''

    sortedNumber = sorted(list(numberStr), reverse=True)

    for i in sortedNumber:
        answer += i
    if int(answer) % 30 == 0:
        print(answer)
    else:
        print(-1)