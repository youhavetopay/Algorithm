import sys

a = int(sys.stdin.readline())
for line in range(a):
    print(sum(map(int, sys.stdin.readline().split(','))))
    # b = sys.stdin.readline()
    # print(int(b[0])+int(b[2]))