# 다트 게임

def solution(a):
    locaction = 0
    scores = [0,0,0]
    arrCount = 0
    for i in range(2,len(a)):
        scoreStr = ''
        print(a[i-1],a[i], arrCount)
        if a[i].isnumeric() or arrCount == 2: # 해당문자가 숫자인지 판별
            if a[i-1].isnumeric() and arrCount != 2:
                continue

            scoreStr = a[locaction:i]
            if arrCount == 2:
                scoreStr = a[locaction:]
            print(scoreStr)
            locaction = i
            
            isnumber = 0
            if scoreStr[:2].isnumeric():
                isnumber = 1
            
            for j in range(1,len(scoreStr)):
                if scoreStr[j] == 'S':
                    if isnumber == 1:
                        scores[arrCount] = int(scoreStr[:2])
                    else:
                        scores[arrCount] = int(scoreStr[0])
                elif scoreStr[j] == 'D':
                    if isnumber == 1:
                        scores[arrCount] = int(scoreStr[:2]) ** 2
                    else:
                        scores[arrCount] = int(scoreStr[0]) ** 2
                elif scoreStr[j] == 'T':
                    if isnumber == 1:
                        scores[arrCount] = int(scoreStr[:2]) ** 3
                    else:
                        scores[arrCount] = int(scoreStr[0]) ** 3

                elif scoreStr[j] == '*':
                    if arrCount != 0:
                        scores[arrCount-1] = scores[arrCount-1] * 2
                    scores[arrCount] = scores[arrCount] * 2

                elif scoreStr[j] == '#':
                    scores[arrCount] = scores[arrCount] * -1
            if arrCount == 2:
                break
            arrCount += 1
    
    return sum(scores)
a = '10S10D0T'

print(solution(a))
    