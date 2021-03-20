m = int(input())
list1 = list(map(int, input().split()))

dp = [0]

dp[0] = list1[0]

for i in range(m):
    for j in range(0, len(dp)):
        

        if list1[i] == dp[j]:
            break

        if list1[i] < dp[j]:
            dp[j] = list1[i]
            break
            
        elif max(dp) < list1[i]:
            dp.append(list1[i])
            break

        
print(len(dp))