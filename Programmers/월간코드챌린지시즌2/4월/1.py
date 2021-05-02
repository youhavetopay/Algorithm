def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer

list1 = [4,7,12]

list2 = ['true','false','true']

print(solution(list1, list2))