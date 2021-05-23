# 큐

import sys

input = sys.stdin.readline

orderCount = int(input())
queue = []

for i in range(orderCount):
    orderStr = input().split()
    if orderStr[0] == 'push':
        queue.append(int(orderStr[1]))
    
    elif orderStr[0] == 'pop':
        if queue == []:
            print(-1)
        else:
            print(queue.pop(0))
    
    elif orderStr[0] == 'size':
        print(len(queue))
    
    elif orderStr[0] == 'empty':
        if queue == []:
            print(1)
        else:
            print(0)
    
    elif orderStr[0] == 'front':
        if queue == []:
            print(-1)
        else:
            print(queue[0])
    
    elif orderStr[0] == 'back':
        if queue == []:
            print(-1)
        else:
            print(queue[-1])