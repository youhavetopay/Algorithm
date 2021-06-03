def solution(arr):
    answer = []
    dic = {}
    for i in range(len(arr)):
        try:
            dic[arr[i]] += 1
        except KeyError:
            dic[arr[i]] = 1
    
    for key, value in dic.items():
        if value > 1:
            answer.append(value)

    if answer == []:
        return -1
        
    return answer


list1 = [1,2,3,3,3,3,4,4]
list2 = [3,2,4,4,2,5,2,5,5]
list3 = [3,5,7,9,1]

print(solution(list1))
print(solution(list2))
print(solution(list3))