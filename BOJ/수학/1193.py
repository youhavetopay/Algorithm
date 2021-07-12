# 분수찾기

find = int(input())

answer = [1, 2]
count = 1

if find == 1:
    print('1/1')
else:
    frist, second = 1, -1
    checkBin = 0
    for i in range(find-2):
        
        if checkBin == 0:
            if answer[1]==1:
                answer[0] +=1
                frist, second = -1, 1
                checkBin = 1
                continue

        else:
            if answer[0] == 1:
                answer[1] +=1
                frist, second = 1, -1
                checkBin = 0
                continue

        answer[0] += frist
        answer[1] += second

        
       
    print(str(answer[0])+'/'+str(answer[1]))