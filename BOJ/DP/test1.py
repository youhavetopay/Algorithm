bord = [
    [3,7,9,2,7],
    [9,8,3,5,5],
    [1,7,9,8,5],
    [3,8,6,4,10],
    [6,3,9,7,8],
    [3,7,9,2,7],
    [9,8,3,5,5],
    [1,7,9,8,5],
    [3,8,6,4,10],
    [6,3,9,7,8],
    [3,7,9,2,7],
    [9,8,3,5,5],
    [1,7,9,8,5],
    [3,8,6,4,10],
    [6,3,9,7,8],
    [3,7,9,2,7],
    [9,8,3,5,5],
    [1,7,9,8,5],
    [3,8,6,4,10],
    [6,3,9,7,8]
]

answer = []
total = 3

location_x = 0
location_y = 0
print(len(bord), len(bord[0]))
while True:
    if location_x == len(bord[0])-1 and location_y == len(bord)-1:
        answer.append([location_y, location_x])
        break

    answer.append([location_y, location_x])
    if location_x+1<len(bord[0]) and location_y+1<len(bord):
        
        if bord[location_y][location_x+1] < bord[location_y+1][location_x]:
            location_y +=1
            total += bord[location_y][location_x]
        else:
            location_x +=1
            total += bord[location_y][location_x]

    elif location_x+1 >= len(bord[0]):
        location_y +=1
        total += bord[location_y][location_x]

    elif location_y+1 >= len(bord):
        location_x +=1
        total += bord[location_y][location_x]

print(answer)
print(total)