# 수 찾기 

# 난 해쉬로 함

from collections import defaultdict

n = int(input())

list1 = list(map(int, input().split()))

hashTable = defaultdict(list)

for value in list1:
    hashTable[value] = True

m = int(input())

list2 = list(map(int, input().split()))

answers = []

for obj in list2:
    if hashTable[obj] == True:
        answers.append(1)
    else:
        answers.append(0)

# for obj in list2:

#     start, end = 0, n-1
#     mid = round((start + end) / 2)

#     while True:

#         if list1[0] > obj or list1[-1] < obj:
#             answers.append(0)
#             break

#         if list1[mid] < obj:
#             start = mid
#         elif list1[mid] > obj:
#             end = mid
#         elif list1[mid] == obj:
#             answers.append(1)
#             break

#         if mid + 1 < n and mid - 1 > -1:
#             if list1[mid-1] < obj and obj < list1[mid +1]:
#                 answers.append(0)
#                 break

#         mid = round((start + end) / 2)
        
for i in answers:
    print(i)