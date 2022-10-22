import sys
input = sys.stdin.readline

time_table = []
N = int(input())
for i in range(N):
    time = list(map(int, input().split(' ')))
    time_table.append(time)

sorted_time_table = sorted(time_table, key=lambda x : (x[1], x[0]))
answer = 1
last_end_time = sorted_time_table[0][1]

#print(sorted_time_table)
for idx, time in enumerate(sorted_time_table):
    if idx > 0:
        if last_end_time <= time[0]:
            last_end_time = time[1]
            answer += 1

print(answer)