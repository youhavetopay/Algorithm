# 캠핑

count = 1
while True:
    
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    answer = ((V//P) * L)

    if V%P < L:
        answer += V%P
    else:
        answer += L
    
    print('Case %d: %d'%(count, answer))

    count += 1