dp = [-1] *10002
maxValue = 987654321
numList = ''
def classify(a, b):
    
    M = numList[a:b]
    print('print M ', M)
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
            return 5
    
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

    if dp[begin] != -1:
        return dp[begin]

    ret = maxValue

    for L in range(3, 6):
        
        if begin + L <= len(numList):
            print('begin  if in   ',begin, L, begin+L)
            new_ret = memorize(begin + L)+classify(begin, begin + L)
            print(ret, new_ret)
            ret = min(ret, new_ret)
        else:
            break
    
    dp[begin] = ret

    return dp[begin]

numList = input()
print(len(numList))
print(memorize(0))

