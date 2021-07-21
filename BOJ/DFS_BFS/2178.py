# 미로찾기

n, m = map(int, input().split())

board = []

for _ in range(n):
    tempList = list(input())
    board.append(tempList)

queue = []

nowLoc = [0,0]

answer = 1
while nowLoc != [n-1,m-1]:
    