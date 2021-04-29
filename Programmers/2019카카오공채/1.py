#실패율

"""
내가 한거 
테스트케이스22번 시간초과 ㅜㅜ..
4000ms정도 나와야 하지만 8000ms이상 나옴
"""
def solution1(N, stages):
    answer = []
    stageInfo = [[0,0,x+1] for x in range(N+1)]

    for i in stages:
        for j in range(i):
            stageInfo[j][1] += 1
            if j < i-1:
                stageInfo[j][0] += 1
        
    print(stageInfo)
    dicStageInfo = {}
    
    for i in range(N):
        if stageInfo[i][1] == 0:
            dicStageInfo[stageInfo[i][2]] = 0
        else:
            dicStageInfo[stageInfo[i][2]] = (stageInfo[i][1] - stageInfo[i][0]) / stageInfo[i][1]
        
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

print(solution(4, [4,4,4,4,4]))

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))