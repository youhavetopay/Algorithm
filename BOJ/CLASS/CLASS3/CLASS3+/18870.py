import sys
input = sys.stdin.readline

N = int(input())

X = list(map(int, input().split(' ')))

soted_X = sorted(X)

number_dict = {}

number_dict[soted_X[0]] = 0
for i, num in enumerate(soted_X):
    if i > 0 and soted_X[i-1] < num:
        number_dict[num] = number_dict[soted_X[i-1]] + 1

for num in X:
    print(number_dict[num], end=' ')