# 비밀지도
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tempList1 = list(bin(arr1[i]))[2:]
        tempList2 = list(bin(arr2[i]))[2:]
        while len(tempList1) < n:
            tempList1.insert(0,'0')
        while len(tempList2) < n:
            tempList2.insert(0,'0')

        code = ''
        for count in range(n):
            if int(tempList1[count]) or int(tempList2[count]):
                code += '#'
            else:
                code += ' '
        answer.append(code)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

if 0 or 0:
    print(1)
else:
    print(0)