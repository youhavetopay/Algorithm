typeValues = ['+FX', '-FX', '+YF', '-YF']
conv = [[0,2], [1,2], [0,3], [1,3]]

memoi = [[-1 for _ in range(20)] for _ in range(51)]

st = [-1]*51

count, p, l = map(int, input().split())
dragon = 'FX'
answer = dragon

# 이거는 완전탐색으로 하는거 --> 구현만 됨 높은 숫자는 안됨

# for level in range(count):
#     i = 0
#     while i < len(dragon):
        
#         if dragon[i] == 'X':
#             dragon = dragon[0:i]+'X+YF'+dragon[i+1:len(dragon)]
#             i += 4
#             continue
#         if dragon[i] == 'Y':
#             dragon = dragon[0:i]+'FX-Y'+dragon[i+1:len(dragon)]
#             i += 4
#             continue
        
#         i += 1

# print(dragon[p-1:p+l-1])

maxValue = 1000000000 + 1

length = [0] * 51

# 해당 세대의 문자 길이 저장
"""
length[i] = length[i-1] * 2 + 2
"""
def precalc():
    length[0] = 1
    for i in range(1, 51):
        length[i] = min(maxValue, length[i-1] * 2 + 2)

EXPAND_X = 'X+YF'
EXPAND_Y = 'FX-Y'

def expand(dragonCurve, generations, skip):
    if generations == 0:
        assert skip < len(dragonCurve)
        return dragonCurve[skip]
    
    for i in range(len(dragonCurve)):
        if dragonCurve[i] == 'X' or dragonCurve[i] == 'Y':
            
            if skip >= length[generations]:
                skip -= length[generations]

            elif dragonCurve[i] == 'X':
                return expand(EXPAND_X, generations -1, skip)
            
            else:
                return expand(EXPAND_Y, generations-1, skip)
        
        elif skip > 0:
            skip -= 1
        
        else:
            return dragonCurve[i]

precalc()

for i in range(l):
    print(expand('FX', count, p+i-1), end='')