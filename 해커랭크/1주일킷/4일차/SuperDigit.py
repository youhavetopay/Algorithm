def makeSuperDigit(n):
    super_num = sum(map(int, n))
    super_num_length = len(str(super_num))

    if super_num_length > 1:
        super_num = makeSuperDigit(str(super_num))
    
    return super_num

def superDigit(n, k):
    super_num = sum(map(int, n))
    answer = makeSuperDigit(str(super_num*k))

    return answer


print(superDigit('148', 3))
