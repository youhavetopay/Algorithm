# 카펫

def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if ((yellow/i) + 2) * 2 + (2 * i) == brown:
            x = yellow // i + 2
            y = i + 2
            if x > y:
                answer.append(x)
                answer.append(y)
            else:
                answer.append(y)
                answer.append(x)
            break

    return answer