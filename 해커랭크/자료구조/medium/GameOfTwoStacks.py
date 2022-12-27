def twoStacks(maxSum, a, b):
    # Write your code here

    max_turn_count = 0
    now_sum = 0
    a_idx = 0
    b_idx = 0


    # 일단 첫번째 스택만 생각하고 넣기
    for num in a:
        if now_sum + num > maxSum:
            break

        now_sum += num
        a_idx += 1
    
    max_turn_count = a_idx
    
     
    for num in b:
        now_sum += num
        b_idx += 1

        # 만약에 두번째 스택의 요소를 넣었는데 점수가 넘었다면
        # 첫번째에서 담았던거 빼기
        while now_sum > maxSum and a_idx > 0:
            now_sum -= a[a_idx-1]
            a_idx -= 1
        
        # 지금 최대 점수가 안넘었다면 
        # 이전 값과 비교해서 더 큰 값으로
        if now_sum <= maxSum:
            max_turn_count = max(a_idx + b_idx, max_turn_count)

    return max_turn_count


a1 = [7, 15, 12, 0, 5, 18, 17, 2, 10, 15, 4, 2, 9, 15, 13, 12, 16]
b1 = [12, 16, 6, 8, 16, 15, 18, 3, 11, 0, 17, 7, 6, 11, 14, 13, 15, 6, 18, 6, 16, 12, 16, 11, 16, 11]
m1 = 62

# print(twoStacks(m1, a1, b1))


a1 = '4 2 4 6 1'
b1 = '2 1 8 5'
m1 = 10
a1 = list(map(int, a1.split(' ')))
b1 = list(map(int, b1.split(' ')))

print(twoStacks(m1, a1, b1))
