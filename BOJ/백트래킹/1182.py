import sys
input = sys.stdin.readline

# N, S = map(int, input().split())

# array = list(map(int, input().split()))

N, S = 5, 0

array = [-7, -3, -2, 5, 8]

answer = 0


# # 이거 잘 기억하기
# # 모든 부분 수열 만들어주는 거임
# for i in range(1, 1 << N):
#     sumValue = 0
#     for j in range(N):
#         if i & (1 << j):
#             sumValue += array[j]
    
#     if sumValue == S:
#         answer += 1

# print(answer)

can = set()
not_can = set()

for i in range(N):
    now = array[i]

    def dfs(now_sum, seleted, last):
        global N, answer
        
        key = tuple(sorted(seleted))
        print(key)
        if key in not_can:
            return

        if now_sum == S and key not in can:
            can.add(key)
            answer += 1
        
        for next in range(last+1, N):
            if next not in seleted:
                dfs(now_sum + array[next], seleted + [next], next)


        not_can.add(key)

    dfs(now, [i], -1)

print(can)
print(not_can)
print(answer)