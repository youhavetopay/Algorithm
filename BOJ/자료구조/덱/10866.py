# 덱

import sys

input = sys.stdin.readline

orderCount = int(input())

deque = []

for i in range(orderCount):
    orderStr = input().split()

    if orderStr[0] == 'push_front':
        deque.insert(0,int(orderStr[1]))

    elif orderStr[0] == 'push_back':
        deque.append(int(orderStr[1]))
    
    elif orderStr[0] == 'pop_front':
        if deque == []:
            print(-1)
        else:
            print(deque.pop(0))
    
    elif orderStr[0] == 'pop_back':
        if deque == []:
            print(-1)
        else:
            print(deque.pop())
    
    elif orderStr[0] == 'size':
        print(len(deque))
    
    elif orderStr[0] == 'empty':
        if deque == []:
            print(1)
        else:
            print(0)
    
    elif orderStr[0] == 'front':
        if deque == []:
            print(-1)
        else:
            print(deque[0])
    
    elif orderStr[0] == 'back':
        if deque == []:
            print(-1)
        else:
            print(deque[-1])
