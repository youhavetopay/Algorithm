# number = int(input())

def star(num):
    pass


for i in range(3):
    count = 1
    for j in range(9):
        if i == 1 and j == count:
            print(' ', end='')
            count+=3
        else:
            print('*', end='')
    print()