# 프린터 큐

import sys

input = sys.stdin.readline

count = int(input().strip())
answers = []

for i in range(count):
    docCount, findDocLoc = map(int, input().strip().split())
    priority = list(map(int, input().strip().split()))
    queue = [[x, y] for x, y in enumerate(priority)]
    
    answer = 0
    if len(priority) > 1:
       
        while True:     
            popValue = []

            checkList = [x[1] for x in queue]

            if len(checkList) <= 1:
                answer+= 1
                popValue = queue.pop(0)
            
            elif checkList[0] < max(checkList[1:]):
                queue.append(queue.pop(0))
            else:
                answer+= 1
                popValue = queue.pop(0)
               
            
            if popValue != [] and popValue[0] == findDocLoc:
                break
    
    else:
        answer = 1
    
    answers.append(answer)

for i in answers:
    print(i)