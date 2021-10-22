def gridSearch(R, C, r,c,G, P):
    # Write your code here
    
    if R == r and C == c:
        for g, p in zip(G, P):
            if g != p:
                return 'NO'
        else:
            return 'YES'

    for Row in range(R - r+1):
        for col in range(C-c+1):
            for row in range(r):
                # print(row+Row, col, col+c, G[row+Row][col:col+c], P[row])
                if G[row+Row][col:col+c] != P[row]:
                    break
            else:
                return 'YES'
    
    return 'NO'

G1 = [
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [3,19,1,2,3,4,5,6,7,8],
    [3,3,1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
    [1,2,3,4,5,6,7,8,9,0],
]

P1 = [
    [3,3],
    [3,3]
]

G2 = [
    [1,2,3,4,1,2],
    [5,6,1,2,1,2],
    [1,2,3,6,3,4],
    [7,8,1,2,8,8],
]
P2 = [
    [1,2],
    [3,4]
]

print(gridSearch(4, 6, 2,2,G2, P2
))