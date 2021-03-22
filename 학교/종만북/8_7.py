dp = [-1] *10002
maxValue = 987654321
numList = ''
def classify(a, b):
    
    M = numList[a:b]
    print(M)
    if M == str(M[0]*len(M)):
        return 1

    diff = int(M[1]) - int(M[0])
    seq = True
    for i in range(1,  b-a):
        if int(M[i]) - int(M[i-1]) == diff: 
            continue
        seq = False
        break

    if seq:
        if diff == -1 or diff == 1: 
            return 2
        else:
            return
    
    alternating = True
    for i in range(len(M)):
        if M[i] != M[i%2]:
            alternating = False
    
    if alternating: 
        return 4


    return 10

        

def memorize(begin):
    
    if begin >= len(numList):
        return 0
    ret = dp[begin]

    if ret != -1:
        return ret
    
    ret = maxValue

    for L in range(3, 6):
        if begin + L <= len(numList):
            ret = min(ret, classify(begin, begin + L)+memorize(begin + L))
    
    dp[begin] = ret

    return dp[begin]

numList = input()

print(memorize(0))
