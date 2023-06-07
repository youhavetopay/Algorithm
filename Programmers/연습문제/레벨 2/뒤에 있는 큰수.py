def solution(numbers):
    answer = []


    stack = [[0, numbers[0]]]

    for i in range(1, len(numbers)):

        while stack and stack[-1][1] < numbers[i]:
            answer.append(numbers[i])
            stack.pop()

        stack.append([i, numbers[i]])
        print(stack, answer, i)

    print(answer, stack)

    while stack:
        i, _ = stack.pop(0)
        answer.insert(i, -1)

    return answer

print(solution([2, 3, 3, 5]))

[2, 3, 3, 5]

[9, 1, 5, 3, 6, 2]
