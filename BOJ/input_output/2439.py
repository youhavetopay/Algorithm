value = int(input())

for i in range(1, value+1):
    print(' '*(value-i), end='')
    print('*'*i)
