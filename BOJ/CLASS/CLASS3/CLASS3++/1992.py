# 1992 쿼드트리
import sys
input = sys.stdin.readline

N = int(input())

video = []
for _ in range(N):
    video.append(input().strip())

video_str = ''
def checkVideo(x, y, length):
    value = video[y][x]
    for i in range(y, y+length):
        for j in range(x, x+length):
            if value != video[i][j]:
                return [False, value]

    return [True, value]

def splitVideo(x, y, length):
    global video_str
    result = checkVideo(x, y, length)
    if result[0]:
        video_str += result[1]
        return
    else:
        video_str += '('
        new_length = int(length/2)
        splitVideo(x, y, new_length)
        splitVideo(x+new_length, y, new_length)
        splitVideo(x, y+new_length, new_length)
        splitVideo(x+new_length, y+new_length, new_length)

        video_str += ')'

splitVideo(0, 0, N)
print(video_str)