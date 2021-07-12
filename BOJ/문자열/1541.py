# 잃어버린 괄호

way = input()

wayList = list(way.split('-'))

answer = 0

for index, value in enumerate(wayList):
    plusValue = 0
    if '+' in value:
        plusStrList = list(value.split('+'))
        for num in plusStrList:
            plusValue += int(num)
    else:
        plusValue += int(value)

    if index < 1:
        answer += plusValue
    else:
        answer -= plusValue

print(answer)