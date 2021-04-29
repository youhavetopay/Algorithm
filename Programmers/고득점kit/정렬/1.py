# K번째 수

def solution(array, commands):
    answer = []

    for tempList in commands:
        sortedList = sorted(array[tempList[0]-1:tempList[1]])
        answer.append(sortedList[tempList[2]-1])


    return answer

list1 = [1, 5, 2, 6, 3, 7, 4]
list2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print()

print(solution(list1, list2))