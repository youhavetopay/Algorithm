def insertStack(num, stack, idx, max_idx):

    idx += 1

    stack[idx] = num

    # 스택의 최대값 갱신
    if max_idx == -1 or stack[idx] > stack[max_idx]:
        max_idx = idx

    return stack, idx, max_idx

def popStack(stack, idx, max_idx):

    last_idx = idx

    stack[idx] = -1

    idx -= 1

    # 스택의 최대값 갱신
    if max_idx == last_idx and idx != -1:
        # 스택의 최대 길이가 10^5이라서 전부다 볼 필요는 없느니
        # top 까지만 검색
        check_stack = stack[:idx+1]
        max_idx = check_stack.index(max(check_stack))

    return stack, idx, max_idx


def getMax(operations):
    # Write your code here

    # 명령어의 개수로 최대 스택의 크기를 결정
    max_length = len(operations) 

    # 스택 초기화
    stack = [-1] * max_length

    # top
    top_idx = -1

    # 최대값의 위치
    max_idx = -1

    answer = []

    for oper in operations:
        if oper[0] == '1':
            number = list(map(int, oper.split(' ')))[1]
            stack, top_idx, max_idx = insertStack(number, stack, top_idx, max_idx)
        elif oper[0] == '2':
            stack, top_idx, max_idx = popStack(stack, top_idx, max_idx)

        elif oper[0] == '3':
            answer.append(stack[max_idx])

    return answer

#a = ['1 83', '3', '2', '1 76']
a = [
    '1 97',
    '2',
    '1 20',
    '2',
    '1 26',
    '1 20',
    '2',
    '3',
    '1 91',
    '3'
]
print(getMax(a))