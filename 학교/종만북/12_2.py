count = int(input())
answers = []
for i in range(count):
    baseCount = int(input())
    baseLength = [[1001 for _ in range(baseCount)] for _ in range(baseCount)]
    baseLocations = []

    tempList = []

    for _ in range(baseCount):
        baseLocations.append(list(map(float, input().split())))

    for i in range(baseCount):
        for j in range(i+1,baseCount):
            baseLength[i][j] = round(((baseLocations[i][0] - baseLocations[j][0])**2 + (baseLocations[i][1] - baseLocations[j][1])**2)**0.5, 2)

    baseLength[baseCount-1][baseCount-1] = 0

    for temp in baseLength:
        tempList.append(min(temp))

    answers.append(max(tempList))

for i in answers:
    print('%.2f'%i)