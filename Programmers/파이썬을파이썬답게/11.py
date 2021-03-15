import itertools

def solution(mylist):

    return sorted(list(map(list, itertools.permutations(mylist))))


list1 = [1, 2, 3]

print(solution(list1))