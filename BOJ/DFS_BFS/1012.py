# 유기농 배추 1012

case = int(input())
answers = []
while case > 0:
    M, N, K = map(int, input().split())

    X = []
    for i in range(K):
        X.append(list(map(int, input().split())))

    visited = [False] * K
    componet = 1
    stack = [X[0]]
    X.pop(0)

    while True:
        tempList = stack[-1]

        # 위
        if [tempList[0], tempList[1] - 1] in X:
            stack.append([tempList[0], tempList[1] - 1])
        
        # 오른쪽
        if [tempList[0] + 1, tempList[1]] in X:
            stack.append([tempList[0] + 1, tempList[1]])
        
        # 아래
        if [tempList[0], tempList[1] + 1] in X:
            stack.append([tempList[0], tempList[1] + 1])

        # 왼쪽
        if [tempList[0] - 1, tempList[1]] in X:
            stack.append([tempList[0] - 1, tempList[1]])
        
        if len(stack) != 0:
            stack.remove(tempList)
        if tempList in X:
            X.remove(tempList)

        if len(stack) == 0:
            if len(X) == 0:
                break
            stack.append(X[0])
            componet += 1
            X.pop(0)

    answers.append(componet)
    case -= 1

for i in answers:
    print(i)