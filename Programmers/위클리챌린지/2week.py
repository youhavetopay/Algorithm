
def solution(scores):
    answer = ''

    studentCount = len(scores)

    for x in range(studentCount):

        minInfo = [1000,-1, 0]
        maxInfo = [-1, -1, 0]
        for y in range(studentCount):
            score = scores[y][x]
            if score <= minInfo[0]:
                if score == minInfo[0]:
                    minInfo[2] += 1
                else:
                    minInfo[0] = score
                    minInfo[1] = y
                    minInfo[2] = 1
            
            if score >= maxInfo[0]:
                if score == maxInfo[0]:
                    maxInfo[2] += 1
                else:
                    maxInfo[0] = score
                    maxInfo[1] = y
                    maxInfo[2] = 1
        
        total = 0
        flag = False
        for y in range(studentCount):
            if y == x and minInfo[1] == y and minInfo[2] == 1:
                flag = True
                continue
            if y == x and maxInfo[1] == y and maxInfo[2] == 1:
                flag = True
                continue
            total += scores[y][x]
        if flag == True:
            avg = total / (studentCount -1)
        else:
            avg = total / studentCount

        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

s1 = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
s2 = [[50,90],[50,87]]
s3 = [[70,49,90],[68,50,38],[73,31,100]]

print(solution(s1))