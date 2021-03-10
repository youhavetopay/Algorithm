def solution(mylist):
    answer = []
    for i in mylist:
        for j in i:
            answer.append(j)
    return answer

list1 = [['A', 'B'], ['X', 'Y'], ['1']]
print(solution(list1))


# 2차원 리스트 1차원으로 변환 방법들
# sum이 제일 간편할듯


# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))