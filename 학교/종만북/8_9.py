# Quantization
import copy
numLength, numKind = map(int, input().split())

A = sorted(list(map(int, input().split())))

INF = 987654321

# 부분합
pSum = [ 0 for _ in range(101)]

# 제곱의 부분합
pSqSum = [0 for _ in range(101)]
sumValue = 0
sqSum = 0
cache = [[-1 for _ in range(11)] for _ in range(101)]

# 부분 합 계산
def precalc():
    pSum[0] = A[0]
    pSqSum[0] = A[0] * A[0]

    for i in range(1, numLength):
        pSum[i] = pSum[i-1] + A[i]
        pSqSum[i] = pSqSum[i-1] + A[i] * A[i]


"""
A[lo] ... A[hi] 구간을 하나의 숫자로 표현할 때 최소 오차 합을 계산

"""
def minError(lo, hi):
    # 부분합을 이용해서 합을 구함 ㄷㄷ
    if lo == 0:
        sumValue = pSum[hi]
        sqSum = pSqSum[hi]
    else:
        sumValue = pSum[hi] - pSum[lo-1]
        sqSum = pSqSum[hi] - pSqSum[lo-1]

    # 평균을 반올림한 값으로 이 수들을 표현
    m = round(sumValue/ (hi-lo+1))
    # int(0.5 + float(sum / (hi - lo + 1)))

    # sum(A[i]-m)^2를 전개한 결과를 부분 합으로 표현
    ret = sqSum - 2 * m * sumValue + m * m * (hi - lo + 1)
    return ret

def quantize(front, parts):

    # 기저 사례: 모든 숫자를 다 양자화 했을 때
    if front == numLength:
        return 0

    # 기저 사례: 숫자는 아직 남았는데 더 묶을 수 없을 대 아주 큰 값을 반환
    if parts == 0:
        return INF
    
    ret = copy.deepcopy(cache[front][parts])
    if ret != -1:
        return ret
    
    ret = INF
    partSize = 1

    # 조각의 길이를 변화시켜 가며 최소치를 찾는다.
    while front + partSize <= numLength:
        ret = min(ret, minError(front, front+ partSize -1) + 
                        quantize(front + partSize, parts -1))
        partSize += 1
    
    return ret

precalc()
print(quantize(0, numKind))