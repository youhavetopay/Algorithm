value = int(input())

values = list(map(int, input().split(' ')))

values.sort()

print(values[0], values[-1])

# print(min(values), max(values))
# 정렬보단 시간 복잡도가 낮음 (탐색이라서)