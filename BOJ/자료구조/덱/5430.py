# AC

import sys

input = sys.stdin.readline

testCount = int(input().strip())

answers = []

for i in range(testCount):
    orderStr = input().strip()
    
    arrSize = int(input().strip())

    array = input().strip()[1:-1].split(',')

    if 'RR' in orderStr:
        orderStr.replace('RR', '')

    if orderStr.count('D') > arrSize:
        answers.append('error')
    elif arrSize < 1:
        answers.append('[]')
    else:
        reverseFlag = 1
        reverseLoc = -1
        forwardLoc = 0
        for order in orderStr:
            if order == 'R':
                if reverseFlag == 1:
                    reverseFlag = -1
                else:
                    reverseFlag = 1
                
            else:
                if reverseFlag == 1:
                    array[forwardLoc] = 0
                    forwardLoc += 1
                else:
                    array[reverseLoc] = 0
                    reverseLoc -= 1

        if 0 in array:
            array = [item for item in array if item != 0]
        if reverseFlag == -1:
            array.reverse()
            
        if array == []:
            answers.append('[]')
        else:
            answers.append(array)

for answer in answers:
    if answer == '[]':
        print('[]')
    elif answer[0] == 'e':
        print('error')
    else:
        a = '['
        for word in answer:
            a = a+ word+','
        
        print(a[:-1]+']')
