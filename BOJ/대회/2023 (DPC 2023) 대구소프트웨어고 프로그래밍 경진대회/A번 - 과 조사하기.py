import sys
input = sys.stdin.readline

P = int(input())

soft = 0
embed = 0
ai = 0
frash = 0

for _ in range(P):

    G, C, N = map(int, input().split())
    if G == 1:
        frash += 1
        continue
    
    if C in [1, 2]:
        soft += 1
    elif C == 3:
        embed += 1
    elif C == 4:
        ai += 1
    
    

print(soft)
print(embed)
print(ai)
print(frash)