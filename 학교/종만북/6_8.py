# 시계 맞추기  문제 아이디 : CLOCKSYNC 난이도 중

# switchs = [
#     [0,1,2],
#     [3,7,9,11],
#     [4,10,14,15],
#     [0,4,5,6,7],
#     [6,7,8,10,12],
#     [0,2,14,15],
#     [3,14,15],
#     [4,5,7,14,15],
#     [1,2,3,4,5],
#     [3,4,5,9,13]
# ]

# answer = -1

# list1 = [12, 6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]
# list2 = [12,9,3,12,6,6,9,3,12,9,12,9,12,12,6,6]
# imp = [1, 2, 4, 5, 7, 8, 10, 11]


# def solution(clockTimes):
#     for i in imp:
#         if i in clockTimes:
#             return -1
    
#     tempList = []

#     for i in range(len(clockTimes)):
#         if clockTimes[i] != 12:
#             tempList.append(i)
    
#     return tempList

# print(solution(list2))



# 문제의 핵심 
# 어떤 스위치든 간에 4번 누르면 처음으로 돌아오기 때문에 
# 각 스위치는 0 ~ 3번만 누름


maxValue = 9999
CLOCK_LENGTH = 16
SWITCHES_LENGTH = 10
linked = [
    'xxxooooooooooooo',
    'oooxoooxoxoxoooo',
    'ooooxoooooxoooxx',
    'xoooxxxxoooooooo',
    'ooooooxxxoxoxooo',
    'xoxoooooooooooxx',
    'oooxooooooooooxx',
    'ooooxxoxooooooxx',
    'oxxxxxoooooooooo',
    'oooxxxoooxoooxoo'
]

#clocks = list(map(int, input().split()))
list1 = [12, 6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]
list2 = [12,9,3,12,6,6,9,3,12,9,12,9,12,12,6,6]

clockTimes = list2
print(len(linked[0]), len(linked))
# 시간이 전부 12시인지 체크하는 함수
def checkTime():
    for time in clockTimes:
        if time != 12:
            return False
    
    return True

# 버튼 누르는 함수
def push(switch):
    for clock in range(16):
        if linked[switch][clock] == 'x':
            clockTimes[clock] += 3

            # 시간 넘었을 때
            if clockTimes[clock] == 15 :
                clockTimes[clock] = 3

def solution(switch):
    
    if switch == 10:
        
        if checkTime():
            return 0
        else:
            return maxValue
    
    ret = maxValue

    for cnt in range(4):
        ret = min(ret, cnt + solution(switch+1))
        push(switch)
    
    return ret

print(solution(0))