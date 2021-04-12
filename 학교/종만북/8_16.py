# 두니발 박사의 탈옥
"""

마르코프 연쇄
N : 마을의 수
D : 탈출 후 지금까지 지난 일수
P : 교도소가 있는 마을 번호

A : 마을간 산길 여부
T : 확률을 계산할 마을 수
Q : 확률을 계산할 마을 번호들

"""
import copy
N, D, P = map(int, input().split())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

T = int(input())

Q = list(map(int, input().split()))

deg = []
cache = [[-0.5 for _ in range(51)] for _ in range(51)]
for i in range(N):
    deg.append(A[i].count(1))

def search3(here, days):
    if days == 0:
        if here == P:
            return 1.0
        else:
            return 0.0
    
    ret = copy.deepcopy(cache[here][days])
    if ret > -0.5: return ret

    ret = 0.0
    for there in range(N):
        if A[here][there]:
            ret += search3(there, days-1) / deg[there]
    
    return ret

for i in Q:
    print(search3(i, D))