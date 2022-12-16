from collections import deque

def equalStacks(h1, h2, h3):
    # Write your code here

    deque_h1 = deque(h1)
    deque_h2 = deque(h2)
    deque_h3 = deque(h3)

    sum_h1 = sum(deque_h1)
    sum_h2 = sum(deque_h2)
    sum_h3 = sum(deque_h3)

    sum_array = [sum_h1, sum_h2, sum_h3]

    if sum_h1 == sum_h2 and sum_h2 == sum_h3:
        return sum_h1

    while sum_h1 != sum_h2 or sum_h2 != sum_h3:

        max_idx = sum_array.index(max(sum_array))

        if max_idx == 0:
            if len(deque_h1) == 0:
                sum_h1 = 0
            else:
                sum_h1 -= deque_h1.popleft()
            
            sum_array[0] = sum_h1
        elif max_idx == 1:
            if len(deque_h2) == 0:
                sum_h2 = 0
            else:
                sum_h2 -= deque_h2.popleft()
            
            sum_array[1] = sum_h2
        else:
            if len(deque_h3) == 0:
                sum_h3 = 0
            else:
                sum_h3 -= deque_h3.popleft()
            
            sum_array[2] = sum_h3
    

    return sum_h1

p1 = [3,2,1,1,1]
p2 = [4,3,2]
p3 = [1,1,4,1]

# p1 =[1, 1, 1, 1, 2,]
# p2 =[3, 7]
# p3 =[1, 3, 1,]

print(equalStacks(p1, p2, p3))