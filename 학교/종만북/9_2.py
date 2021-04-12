#여행 짐 싸기

n, w = map(int, input().split())
BIGINT = -987654321
products = []

for _ in range(n):
    products.append(list(map(str, input().split())))


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
