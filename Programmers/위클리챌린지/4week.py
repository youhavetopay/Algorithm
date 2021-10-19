def solution(table, languages, preference):
    answer = []

    tableDic = {}

    for text in table:
        tempList = list(map(str, text.split(' ')))
        category = tempList[0]
        tableDic[category] = []

        tempList = tempList[1:]
        tempList.reverse()
        tableDic[category] = tempList
    

    maxValue = 0
    for key, value in tableDic.items():

        scores = []

        for index,word in enumerate(languages):
            if word in value:
                scores.append((value.index(word)+1) * preference[index])
        
        sumValue = sum(scores)

        if maxValue < sumValue:
            answer = [key]
            maxValue = sumValue
        elif maxValue == sumValue:
            answer.append(key)

    print(answer)
    return sorted(answer)[0]



t1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
l1 = ["PYTHON", "C++", "SQL"]
p1 = [7, 5, 5]

t2 = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
l2 = ["JAVA", "JAVASCRIPT"]
p2=[7, 5]

print(solution(t1, l1, p1))
print(solution(t2, l2, p2))