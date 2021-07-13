number = int(input())


def fibo(num):
    if num < 1:
        return 0

    elif num == 1:
        return 1
    
    else:
        return fibo(num-1) + fibo(num-2)

print(fibo(number))