a = int(input())

arr = []

for i in range(a):
    b = list(map(int, input().split(' ')))
    arr.append(b)

for i in arr:
    print(i[0]+i[1])
# 이거 65ms?




# 다른사람 풀이
# import sys

# input()
# s = list(sum(map(int, n.split())) for n in sys.stdin)
# 이게 input보다 시간복잡도가 낮음?

# for n in s:
#   print(n)
# 이거 52ms?