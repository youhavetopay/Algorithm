# 스택 수열

import sys

input = sys.stdin.readline

numberCount = int(input().strip())

nowNumber = 1
answers = ''

stack = []
checkValue = 0
for i in range(numberCount):
    number = int(input().strip())
    if nowNumber <= number:
        while nowNumber <= number:
            stack.append(nowNumber)
            nowNumber += 1
            answers += '+'
        stack.pop()
        answers += '-'
    else:
        if stack == []:
            checkValue = 1
            
        if stack[-1] != number:
            checkValue = 1
            
        else:
            stack.pop()
            answers += '-'

if checkValue == 1:
    print('NO')
else:
    for temp in answers:
        print(temp)
    
