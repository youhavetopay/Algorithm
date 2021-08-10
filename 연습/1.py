# list2 = [['9',1]]
# count =0
# while True:
#     list1 = []

#     a = input()
#     b= int(input())

#     list1.append(a)
#     list1.append(b)
#     list2.append(list1)
#     print(list2)
#     count +=1
#     if count > 2:
#         break

count = 0
count2 = 0
count3 = 0
for i in range(6):
    for j in range(60):
        for k in range(60):
        # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
    print(count)
print(count, count2, count3)
print(1575 * 5 + 3600)

list1 = [1,2,3,4,5]

print(list1[0:2], list1[3:])