# import sys

# for line in sys.stdin:
#     print(sum(map(int,line.split())))


try:
    while True:
        a, b = map(int, input().split())
        print(a + b)
except:exit()