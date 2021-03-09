def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i]-mylist[i+1]))
    return answer

list1 = [83, 48, 13, 4, 71, 11]
print(solution(list1))


# 답
# for 문에서 길이가 다른 리스트를 
# zip함수를 쓸땐 길이가 짧은 쪽까지만 반복
def solution2(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer