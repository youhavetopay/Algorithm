import sys
input = sys.stdin.readline

N = int(input())

if 1 <= N <= 2:
    print(1)
elif 3 <= N <= 5:
    print(2)
else:
    print(3)


ant_num = '1'
idx = 1
max_count = 0
# while idx <= N:

#     print(ant_num, idx, max_count)

#     count = 1
#     new_ant_num = ''
#     if idx == 1:
#         new_ant_num = '11'
#         idx += 1
#         continue

#     for j in range(1, len(ant_num)):
#         if ant_num[j-1] == ant_num[j]:
#             count += 1
#         else:
#             max_count = max(max_count, count)
#             new_ant_num += (ant_num[j-1] + str(count))
#             count = 1

#     max_count = max(max_count, count)
#     new_ant_num += (ant_num[-1] + str(count))

    
#     ant_num = new_ant_num
#     idx += 1
# print(max_count)