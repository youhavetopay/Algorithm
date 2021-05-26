# 중복 빼고 정렬하기

import sys

input = sys.stdin.readline

numberCount = int(input().strip())

numberList = list(set(map(int, input().strip().split())))

for i in sorted(numberList):
    print(i, end=' ')