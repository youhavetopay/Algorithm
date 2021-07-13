# 팩토리얼

number = int(input())

def factory(num):
    if num <=1:
        return 1
    else:
        return num*factory(num-1)

print(factory(number))