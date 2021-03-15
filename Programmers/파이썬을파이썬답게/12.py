import collections
my_list = input().strip()
answer = collections.Counter(my_list)

tempAnswer = dict(answer)

realAnswer = [x for x, y in tempAnswer.items() if max(tempAnswer.values()) == y]

print(''.join(sorted(realAnswer)))
# print(answer[1]) # = 4
# print(answer[3])  # = 3
# print(answer[100]) # = 0



