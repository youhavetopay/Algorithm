# 1780 종이의 개수

# 분할정복, 재귀 문제
# 그냥 재귀로 완전탐색으로 품

# 체크하고 아니면 나누고 다시 체크 하는 방식

import sys
input = sys.stdin.readline

N = int(input())
page = []
for _ in range(N):
    temp_board = list(map(int, input().split(' ')))
    page.append(temp_board)

min_page_count = 0
zero_page_count = 0
plus_page_count = 0

def splitPage(n, startX, startY, endX, endY):

    if checkPage(startX, startY, endX, endY):
        return
    
    else:
        split_n = int(n/3)

        for i in range(3):
            for j in range(3):
                splitPage(split_n, startX+(j*split_n), startY+(i*split_n), endX-((2-j)*split_n), endY-((2-i)*split_n))


def checkPage(startX, startY, endX, endY):
    global min_page_count, zero_page_count, plus_page_count

    value = page[startY][startX]
    for y in range(startY, endY+1):
        for x in range(startX, endX+1):
            if page[y][x] != value:
                return False
    
    if value == -1:
        min_page_count += 1
    elif value == 0:
        zero_page_count += 1
    else:
        plus_page_count += 1

    return True

splitPage(N, 0, 0, N-1, N-1)

print(min_page_count)
print(zero_page_count)
print(plus_page_count)