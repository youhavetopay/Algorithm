#실패율

"""
내가 한거 
테스트케이스22번 시간초과 ㅜㅜ..
4000ms정도 나와야 하지만 8000ms이상 나옴
1000ms으로 줄임ㅋ
"""
def solution1(N, stages):
    answer = []
    personsCount = len(stages)
    firstCount = stages.count(1)
    stageInfo = [[firstCount,personsCount]]
    dicStageInfo = {}
    
    if firstCount == 0:
        dicStageInfo[1] = 0
    else:
        dicStageInfo[1] =stages.count(1) / personsCount

    for i in range(2, N+1):
        stagesCount = stages.count(i)
        
        nowPerson = stageInfo[i-2][1] - stageInfo[i-2][0]
        tempList = [stagesCount, nowPerson]
        stageInfo.append(tempList)

        if stagesCount == 0:
            dicStageInfo[i] = 0
        else:
            dicStageInfo[i] = tempList[0] / tempList[1]

    print(stageInfo) 
    print(dicStageInfo)
    
    tempList5 = sorted(dicStageInfo.items(), key= lambda x: x[1], reverse=True)
    print(tempList5)
    for temp in tempList5:
        answer.append(temp[0])
    return answer

def solution(N, stages):
    ans = []
    b = len(stages)
    ans = dict()

    r_ans = []

    for i in range(1, N+1):
        a = 0
        for j in range(len(stages)):
            if i == stages[j]:
                a+=1
        
        if b != 0:
            ans[i] = a/b
            b = b-a
        
        else:
            ans[i] = 0
            break
    
    ans = sorted(ans.items(), key=lambda x : x[1], reverse=True)
    for temp in ans:
        r_ans.append(temp[0])
    return r_ans

# print(solution1(4, [4,4,4,4,4]))

print(solution1(5, []))