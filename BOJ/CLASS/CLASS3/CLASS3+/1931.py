import sys
input = sys.stdin.readline

N = int(input())

time_table = []
for i in range(N):
    time_table.append(list(map(int, input().split(' '))))

print(time_table)