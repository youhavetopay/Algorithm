# 울타리 잘라내기

count = int(input())

pences = list(map(int, input().split()))

# widthCount = pences[:]

# for i in range(count):
#     for j in range(i+1, count):
#         if pences[i] <= pences[j]:
#             widthCount[i] += pences[i]
#         else:
#             break

# print(max(widthCount))
"""
위에껀 시간복잡도가 n^2라서 제한 시간 초과임 ㅋ

"""
# left, right 구간에서 찾아낼 수 있는 가장 큰 사각형의 넓이를 반환한다.
def solution(left, right):

    # 기저사례 : 판자가 하나밖에 없는 경우
    if left == right:
        return pences[left]
    
    # 두 구간으로 문제를 분할함
    mid = int((left + right) /2)

    # 분할한 문제를 각개격파? ㅋㅋㅋ
    ret = int(max(solution(left, mid), solution(mid+1, right)))

    # 부분문제 3: 두 부분에 모두 걸치는 사각형 중 가장 큰 것을 찾는다.
    lo = mid
    hi = mid+1
    height = min(pences[lo], pences[hi])

    # mid, mid +1 만 포함하는 너비 2인 사각형을 고려함
    ret = max(ret, height*2)

    # 사각형이 입력 전체를 덮을 때까지 확장해 나감
    while left < lo or hi < right:

        # 항상 높이가 더 높은 쪽으로 확장한다.
        if hi < right and (lo == left or pences[lo-1] < pences[hi+1]):
            hi+=1
            height = min(height, pences[hi])
        
        else:
            lo -= 1
            height = min(height, pences[lo])
        
        # 확장시킨 후 사각형의 넓이
        ret = max(ret, height * (hi - lo + 1))
    
    return ret
"""
이건 시간복잡도 n log n 임 
병합 정렬이랑 비슷함???
"""

print(solution(0, 6))