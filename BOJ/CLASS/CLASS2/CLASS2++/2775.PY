test_case = int(input())

i = 0

house = [[x for x in range(1, 15)]]
while i < test_case:

    k = int(input())
    n = int(input())

    if len(house)-1 < k:
        while len(house)-1 < k:
            house.append([1])
            for x in range(1, 14):
                house[-1].append(house[-1][x-1] + house[-2][x])
                
    
    print(house[k][n-1])
    i+= 1