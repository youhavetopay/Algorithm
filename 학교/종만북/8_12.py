import math
value = int(input())

if value == 2 or value == 1:
    print(0)
else:
    dp_list = [0 for i in range(value+1)]

    dp_list[1] = 1
    dp_list[2] = 2

    for i in range(3, value+1):
        dp_list[i] = (dp_list[i-1] + dp_list[i-2]) 

    print((dp_list[value]-dp_list[math.floor((value/2))]-dp_list[math.floor((value-2)/2)])%1000000007)