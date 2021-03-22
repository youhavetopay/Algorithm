dp = [-1] *10002
maxValue = 9999999999999

def classify(a, b):

    M = numList[a:(b-a+1)]
    print(len(M))
    if M == str(M[0]*len(M)):
        return 1

    progressive = True
    for i in range(len(M)-1):
        if (M[i+1] - M[i]) != (M[1] - M[0]):
            progressive = False
    
    if (progressive and abs(M[1] - M[0])) == 1:
        return 2
    
    alternating = True
    for i in range(len(M)):
        if M[i] != M[i%2]:
            alternating = False
    
    if alternating: 
        return 4
    if progressive : 
        return 5

    return 10

        

def memorize(begin):
    if begin == len(numList):
        return 0
    ret = dp[begin]

    if ret != -1:
        return ret
    
    ret = maxValue

    for L in range(3, 6):
        if begin + L <= len(numList):
            ret = min(ret, memorize(begin + L)+ classify(begin, begin + L -1))
    
    dp[begin] = ret

    return dp[begin]

numList = input()

print(numList[0:3])