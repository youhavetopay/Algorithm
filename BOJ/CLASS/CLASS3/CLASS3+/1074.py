import sys
input = sys.stdin.readline

def findBoardNumber(start, x1,y1, x2, y2, block):
    now_start = 0
    
    
    return now_start


N, r, c = map(int, input().split(' '))

# r = y 0부터
# c = x 0부터
answer = 0

block = int((2 ** (N)))

print(findBoardNumber(0, 0, 0, c, r, int(block/2)))

# print(block)

# print(answer)
