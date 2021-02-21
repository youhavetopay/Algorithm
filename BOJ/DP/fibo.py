numbers = [-1 for x in range(1000)]

def fibo(value):

    if value == 0:
        return 0
    
    if value == 1:
        return 1

    if numbers[value] != -1:
        return numbers[value]
    else:
        numbers[value] = fibo(value-1) + fibo(value-2)
        return numbers[value]

print(fibo(int(input())))