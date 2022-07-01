import sys
input = sys.stdin.readline

N = int(input())

wating_times = list(map(int, input().split(' ')))

wating_times.sort()

total_time = 0
wating_time = 0
for time in wating_times:
    total_time = (time + total_time)
    wating_time += total_time

print(wating_time)
