count = int(input())

number_count = 0
i = 0

while True:

    check = 0
    flag = False

    if str(i).count('6') >= 3:
        for number in str(i):
            if number == '6':
                check += 1
                if check == 3:
                    number_count += 1
                    flag = True
            else:
                check = 0
    
    if number_count == count:
        print(i)
        break

    i += 1