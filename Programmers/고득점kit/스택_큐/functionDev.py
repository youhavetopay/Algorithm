# 기능 개발

from collections import deque

def solution(progresses, speeds):
    answer = []

    stackPro = deque()
    stackSped = deque()

    for x, y in zip(progresses, speeds):
        stackPro.append(x)
        stackSped.append(y)

    print(stackPro)

    while stackPro != deque():
        count = 0

        for v in list(stackPro):
            if v >= 100:
                stackPro.popleft()
                stackSped.popleft()
                count += 1
            else:
                break

        if count != 0:
            answer.append(count)

        for i, v in enumerate(list(stackSped)):
            stackPro[i] += v

    return answer



pr1 = [93, 30, 55]
sp1 = [1, 30, 5]

pr2 = [95, 90, 99, 99, 80, 99]
sp2 = [1, 1, 1, 1, 1, 1]	

print(solution(pr2, sp2))