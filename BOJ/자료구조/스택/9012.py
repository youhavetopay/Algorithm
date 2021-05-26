# 괄호

import sys

input = sys.stdin.readline

count = int(input().strip())

stack = []

for i in range(count):
    stack = []
    inputStr = input().strip()
    checkValue = 0

    for value in inputStr:
        if value == '(':
            stack.append(value)
        else:
            if stack == []:
                checkValue = 1
                break
            elif stack[-1] != '(':
                checkValue = 1
                break
            else:
                stack.pop()
    
    if checkValue == 1:
        print('NO')
    else:
        if stack == []:
            print('YES')
        else:
            print('NO')      