month, day = map(int, input().split(' '))

dayList = [31, 28, 31, 30, 31,
           30, 31, 31, 30, 31,
           30, 31]

totalDay = 0

for i in range(0, month-1):
    totalDay += dayList[i]

totalDay += day

if totalDay%7 == 0:
    print('SUN')
elif totalDay%7 == 1:
    print('MON')
elif totalDay%7 == 2:
    print('TUE')
elif totalDay%7 == 3:
    print('WED')
elif totalDay%7 == 4:
    print('THU')
elif totalDay%7 == 5:
    print('FRI')
elif totalDay%7 == 6:
    print('SAT')



# x, y = map(int, input().split())
# for i in range(1, x):
#     if i in [1, 3, 5, 7, 8, 10, 12]:
#         y += 31
#     elif i == 2:
#         y += 28
#     else:
#         y += 30
# day_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# print(day_week[y % 7])