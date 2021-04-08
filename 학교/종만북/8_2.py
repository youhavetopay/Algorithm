#와일드 카드 너무 어렵 ㄷㄷ
import copy

"""
-1 은 아직 답이 계산되지 않은 것
 1 은 해당 입력이 서로 대응되는 것
 0 은 해당 입력들이 서로 대응되지 않는 것
"""
cache = [[-1 for _ in range(101)] for _ in range(101)]
# W 는 와일드카드 패턴
W = ''    
# S 는 입력받은 보기들 
S = ''

# 와일드카드 패턴 W가 문자열 S에 대응 되는지 여부를 반환
def mathchMemoized(w, s):
    ret = copy.deepcopy(cache[w][s])
    if ret != -1:
        return ret
    if w < len(W) and s < len(S) and (W[w] == '?' or W[w] == S[s]):
        ret = mathchMemoized(w+1, s+1)
        return ret
    
    if w == len(W):
        if s == len(S):
            ret = 1
        else:
            ret = 0
        return ret
    
    if W[w] == '*':
        if mathchMemoized(w+1, s) or (s <len(S) and mathchMemoized(w, s+1)):
            ret = 1
            return ret
    
    ret = 0
    return ret

W = input()
n = int(input())

words = []

for i in range(n):
    S = input()
    if mathchMemoized(0, 0) == 1:
        words.append(S)

print(sorted(words))

# 시간복잡도 n ^ 2 