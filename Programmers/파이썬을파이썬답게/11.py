import itertools

def solution(mylist):
    answer = []

    for i in mylist:
        answer.append(str(i))
    print(list(map(''.join, itertools.permutations(answer))))


list1 = [1, 2, 3, 4]

solution(list1)