import collections


def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    # 정렬한 다음에 하나 하나 비교하기 다르거나 뒤에 남는게 답
    for a, b in zip(participant, completion):
        if a != b:
            return a

    return participant[-1]




def solution2(participant, completion):
    # Counter : 리스트에 있는 거 딕셔너리 형으로 갯수 셈
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys()))
    return list(answer.keys())[0]
    

list1 = ["leo", "kiki","kiki", "eden"]
list2 = ["eden", "kiki","leo"]


# print(solution(list1, list2))
print(solution2(list1, list2))