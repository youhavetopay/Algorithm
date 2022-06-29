x, y, w, h = map(int, input().split(' '))

answer = min(abs(x-w), abs(y-h), x, y)

print(answer)