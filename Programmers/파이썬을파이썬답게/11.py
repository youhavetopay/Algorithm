import itertools

def solution(mylist):
    # 조합 
    return sorted(list(map(list, itertools.combinations(mylist,2))))


list1 = [1, 2, 3]

print(solution(list1))