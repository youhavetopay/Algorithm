value = int(input())

for i in range(1, value+1):
    print(' '*(value-i) + '*'*i)

for i in range(value-1, 0, -1):
    print(' '*(value-i) + '*'*i)