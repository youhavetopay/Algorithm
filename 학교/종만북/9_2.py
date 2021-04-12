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
n, mainCapacity = map(int, input().split())

volume = [-1 for _ in range(100)]
need = [-1 for _ in range(100)]
cache = [[-1 for _ in range(100)] for _ in range(1001)]

def pack(capacity, item):
    if item == n:
        return 0
    ret = copy.deepcopy(cache[capacity][item])
    if ret != -1:
        return ret
    
    ret = pack(capacity, item +1)

    if capacity>= volume[item]:
        ret = max(ret, pack(capacity - volume[item], item + 1) + need[item])
    
    return ret

