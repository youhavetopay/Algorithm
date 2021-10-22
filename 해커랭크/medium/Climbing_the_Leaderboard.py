# 중복을 허용한 정렬된 수열에 위치 찾기
# 선형탐색하면 시간초과
# 이진탐색으로 하기 !!

def climbingLeaderboard(ranked, player):
    # Write your code here
    
    totalScore = 0
    
    answers = []


    scoreDict = {1:ranked[0]}
    lastIndex = 1
    rangkingNum = 1
    for num in ranked:
        print(scoreDict[lastIndex] , num)
        if scoreDict[lastIndex] > num:
            rangkingNum += 1 
            lastIndex = rangkingNum
            scoreDict[rangkingNum] = num
            

    print(lastIndex, scoreDict)
    
    for score in player:
        
        if score <= scoreDict[lastIndex]: # 점수가 제일 낮은점수랑 똑같거나 낮을때
            if score == scoreDict[lastIndex]: # 공동 꼴등
                answers.append(lastIndex)
                continue
            else:
                answers.append(lastIndex + 1) # 최하위 꼴등
                continue

        if score >= scoreDict[1]: # 1등
            answers.append(1)
            continue
        
        # 선형탐색
        # for key, value in scoreDict.items():
        #     if score >= value:
        #         answers.append(key)
        #         break
        # else:
        #     answers.append(lastIndex+1)

        # 이진탐색
        first = 1
        end = lastIndex
        mid = end // 2
        lastMid = mid
        while True:
            if scoreDict[mid] > score:
                frist = mid
                lastMid = mid
                mid = (end + frist) // 2 
            elif scoreDict[mid] < score:
                end = mid
                lastMid = mid
                mid = end // 2 
            else: # 점수표에 동일한 점수 있으면 같은 등수
                answers.append(mid)
                break

            if lastMid == mid: # 점수가 사이값이면 이전 등수 + 1
                answers.append(lastMid+1)
                break

            # print(scoreDict[mid], score, mid, lastMid)
        
            
    return answers

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))

print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))