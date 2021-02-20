value = int(input())

for i in range(1, value+1):
    if i >= value:
        print('*'*(value*2-1))
        break
    print(' '*(value-i)+'*', end='')
    print(' '*(((i-1)*2)-1), end='')
    if i>=2:
        print('*')
    else:
        print()

# if value == 1:
#     print('*')

# else:
#     print(' '*(value-1)+'*')
#     for i in range(value-2):
#         print(' ' * (value - i - 2) + '*' + ' ' * (2 * i + 1) + '*')
#     print('*'*(value*2-1))