value = int(input())

for i in range(1, value):
    print(' '*(value-i-1)+' *'*i)

print('* '*(value-1)+'*')


# for i in range(1, value+1):
#     print(' '*(value-i)+'* '*i)
# 뒤에 공백 있어도 상관 없는듯?? ㅋㅋㅋㅋ