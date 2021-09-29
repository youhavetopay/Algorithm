# 모의고사

def solution(answers):
    answer = [0,0,0]

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    oneCount = 0
    twoCount = 0
    threeCount = 0

    for i in range(len(answers)):
        if one[oneCount] == answers[i]:
            answer[0] += 1

        if two[twoCount] == answers[i]:
            answer[1] += 1

        if three[threeCount] == answers[i]:
            answer[2] += 1
        
        oneCount += 1
        if oneCount >= 5:
            oneCount = 0
        twoCount += 1
        if twoCount >= 8:
            twoCount = 0
        threeCount += 1
        if threeCount >= 10:
            threeCount = 0
    
    realAnswer = []
    maxValue = max(answer)
    realAnswer.append(answer.index(maxValue)+1)
    answer[answer.index(maxValue)] = 0

    if maxValue == max(answer):
        realAnswer.append(answer.index(maxValue)+1)
        answer[answer.index(maxValue)] = 0

        if maxValue == max(answer):
            realAnswer.append(answer.index(maxValue)+1)
            answer[answer.index(maxValue)] = 0
            
    realAnswer.sort()

    return realAnswer

answers1 = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,1,2,3,1,3,5,1,3,8,7,1,3,6,9,3,1]
answers2 = [1,3,2,4,2]

print(solution(answers1))