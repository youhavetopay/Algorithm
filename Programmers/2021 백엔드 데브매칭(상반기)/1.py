# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = [6,6]

    removeCount = 0
    while 0 in lottos:
        removeCount += 1
        lottos.remove(0)
    
    winCount = 0
    for i in lottos:
        if i in win_nums:
            winCount += 1
    
    if winCount + removeCount == 6:
        answer[0] = 1
    elif winCount + removeCount == 5:
        answer[0] = 2
    elif winCount + removeCount == 4:
        answer[0] = 3
    elif winCount + removeCount == 3:
        answer[0] = 4
    elif winCount + removeCount == 2:
        answer[0] = 5
    elif winCount + removeCount <2:
        answer[0] = 6

    if winCount == 6:
        answer[1] = 1
    elif winCount == 5:
        answer[1] = 2
    elif winCount == 4:
        answer[1] = 3
    elif winCount == 3:
        answer[1] = 4
    elif winCount == 2:
        answer[1] = 5
    elif winCount < 2:
        answer[1] = 6
    
    return answer

list1 = [44, 1, 0, 0, 31, 25]
list2 = [31, 10, 45, 1, 6, 19]

print(solution(list1, list2))