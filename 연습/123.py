class Man():
    
    def __init__(self, answerList, listLen):
        self.manAnswerList = answerList
        self.index = 0
        self.listLen = listLen
        self.answerCount = 0


def solution(answers):
    answer = []
    

    fMan = Man([1,2,3,4,5], 5)

    sMan = Man([2,1,2,3,2,4,2,5], 8)
    
    tMan = Man([3,3,1,1,2,2,4,4,5,5], 10)
    
    for answer in answers:
        if answer == fMan.manAnswerList[fMan.index]:
            fMan.answerCount += 1
        
        if answer == sMan.manAnswerList[sMan.index]:
            sMan.answerCount += 1
        
        if answer == tMan.manAnswerList[tMan.index]:
            tMan.answerCount += 1
        
        fMan.index += 1
        sMan.index += 1
        tMan.index += 1
        
        if fMan.index >= fMan.listLen:
            fMan.index = 0
        
        if sMan.index >= sMan.listLen:
            sMan.index = 0
        
        if tMan.index >= tMan.listLen:
            tMan.index = 0
    
    maxIndex = [-99,-1]
    manAnswerCount = [fMan.answerCount, sMan.answerCount, tMan.answerCount]
    
    for i, v in enumerate(manAnswerCount):
        if maxIndex[0] < v:
            maxIndex[1] = i
            maxIndex[0] = v
            maxIndex = [v,i]
            
        elif maxIndex[0] == v:
            maxIndex.append(v)
            maxIndex.append(i)
    
    if len(maxIndex) >= 4:
        answer = [value+1 for value in sorted(maxIndex[1::2])]
    else:
        answer = [maxIndex[1]+1]
    return answer

print(solution([1,2,3,4,5]))