# 수 정렬하기 3

import sys 


N = int(sys.stdin.readline())

"""
입력의 갯수가 10,000,000개라서 리스트에 담아서 정렬하면 메모리 초과 뜸
입력의 범위가 10000까지라서 dict형태처럼 담아서 하기
"""
list1 = [0 for _ in range(10001)]


for i in range(N):
    list1[int(sys.stdin.readline())] += 1

for index, value in enumerate(list1):
    for j in range(value):
        print(index)