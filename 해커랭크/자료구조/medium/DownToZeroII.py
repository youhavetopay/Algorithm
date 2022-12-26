


# def downToZero(n):
#     # Write your code here

#     max_val = n
#     dp = list(range(max_val+1))

#     for i in range(4, max_val+1):

#         pre_max = dp[i-1] + 1

#         dp[i] = pre_max

#         max_measure = 0
#         for j in range(2, i):
#             if i % j == 0:
#                 max_measure = min(max_measure, j)
            
#             if j * 2 > i:
#                 break        
#         if max_measure != 0:
#             dp[i] = min(dp[i], dp[max_measure]+1)
#     print(dp)

#     return dp[n]

# https://pongdangstory.tistory.com/557
max_n = 10**6
pl = list(range(max_n+1))

for i in range(2, max_n+1):
    cur_val = pl[i]
    prev_val = pl[i-1]

    if cur_val > prev_val + 1:
        pl[i] = prev_val + 1
        cur_val = pl[i]

    for j in range(2, i+1):
        multiple = i * j
        if multiple > max_n:
            break
        init_val = pl[multiple]
        if init_val > cur_val + 1:
            pl[multiple] = cur_val + 1

def downToZero(n):
    # Write your code here

    if n <= 3:
        return n

    return pl[n]

print(downToZero(86))


# q1 = [
#     3,34,86,73,40,7,87,57,81,32,83,39,98,89,86,44,29,36,53,44,72,31,88,30,78,78,55,27,39,42,95,95,25,88,51,6,93,41,90,34,96,68,81,63,6,7,33,26,66,79,4,89,14,33,22,48,17,62,11
# ]

# a1 = [
#     3,6,7,6,5,5,8,6,5,5,7,6,7,8,7,7,7,5,7,7,5,6,7,5,6,6,6,5,6,6,7,7,5,7,6,4,7,6,6,6,5,6,5,5,4,5,6,6,7,7,3,8,6,6,7,5,5,7,6
# ]

# for q, a in zip(q1, a1):
#     if downToZero(q) != a:
#         print(q, a)
#         break
