import collections


# def solution(participant, completion):
#     answer = ''

#     participant.sort()
#     completion.sort()

#     for a, b in zip(participant, completion):
#         if a != b:
#             return a

#     return participant[-1]




def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys()))
    return list(answer.keys())[0]
    

list1 = ["leo", "kiki","kiki", "eden"]
list2 = ["eden", "kiki","leo"]


# print(solution(list1, list2))
print(solution2(list1, list2))