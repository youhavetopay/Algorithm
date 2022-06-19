T = int(input())

now = 0

while now < T:
    now += 1

    count = 0

    H, W, number = map(int, input().split(' '))

    x, y = 0, 0
    for w in range(1, W+1):
        flag = False
        for h in range(1, H+1):
            count += 1
            if count == number:
                flag = True
                x, y = w, h
                break
        if flag:
            break
    
    if x < 10:
        x = '0' + str(x)

    print(str(y) + str(x))