def solution(mylist):
    answer = []
    length = len(mylist)
    for i in range(length):
        temps = []
        for j in range(length):
            temps.append(mylist[j][i])
        answer.append(temps)

    return answer

list1 = [[1,2,3],[4,5,6],[7,8,9]]

print(solution(list1))


# 답
def solution2(mylist):

    # zip : 여러개의 원소들을 하나씩 가져와서 합칠 수 있음
    # * : 여러개의 입력값 리스트로 받을 수 있음
    # **: key value 값을 해쉬? 형태로 받을 때
    answer = list(map(list, zip(*mylist)))
    
    return answer

print(solution2(list1))