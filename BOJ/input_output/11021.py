import sys

a = int(sys.stdin.readline())

for i in range(1,a+1):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d'%(i, a+b))