# 스택

import sys
input = sys.stdin.readline

orderCount = int(input())
stack = []

for i in range(orderCount):
    orderStr = input().split()
    if len(orderStr) > 1:
        stack.append(int(orderStr[1]))
    
    elif orderStr[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
 
    elif orderStr[0] == 'size':
        print(len(stack))
    
    elif orderStr[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    
    elif orderStr[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])