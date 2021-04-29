#여행 짐 싸기

# n, w = map(int, input().split())
# BIGINT = -987654321
# products = []

# for _ in range(n):
#     products.append(list(map(str, input().split())))

"""
temparr = []
def packing(count, weight, hope):
    print(count, weight, hope)
    if count >= n or weight > w:
        return -1
    
    ret = hope

    for i in range(count, n):
        if int(products[i][1]) + weight <= w:
            
            tempValue = packing(i+1, int(products[i][1]) + weight, hope+ int(products[i][2]))
            
            if ret < tempValue:
                print(i+1)
                temparr.append(i+1)
                ret = tempValue
                print(ret, ' hope 값')
    return ret

print(packing(0, 0, 0))
print(temparr)

완전탐색으로 최대 기대값은 출력했지만 뭘 담았는지는 못함

"""
import copy

names = ['' for _ in range(101)]
info = [[0 for _ in range(2)] for _ in range(101)]
cache = [[-1 for _ in range(1001)] for _ in range(101)]

res = []


n, w = map(int, input().split())

for i in range(1, n+1):
    a,b,c = map(str, input().split())
    names[i] = a
    info[i][0] = int(b)
    info[i][1] = int(c)


def choose(now, v):
    if now > n:
        return 0
    
    ret = copy.deepcopy(cache[now][v])

    if ret != -1:
        return ret
    
    ret = choose(now +1, v)
    if v+info[now][0] <= w:
        ret = max(ret, info[now][1]+choose(now + 1, v+info[now][0]))
    
    return ret

def setRes(start, v):
    if start > n:
        return 
    
    if choose(start, v) == choose(start +1, v):
        setRes(start + 1, v)
    
    else:
        res.append(names[start])
        setRes(start +1, v + info[start][0])


maxW = choose(0, 0)
setRes(0,0)

print(maxW, len(res))
for temp in res:
    print(temp) 4