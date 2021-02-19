value = int(input())

for i in range(1, value+1):
    print(' '*(value-i)+'*'*i+'*'*(i-1))


# for i in range(n):
#     print((n-i-1)*' ' + (2*i+1)*'*' )