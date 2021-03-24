n,m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int,input().split()))
dp = [0]

dp[0] = list1[0]

for i in range(n):
    for j in range(0, len(dp)-1):
        
        if list1[i] == dp[j]:
            break

        if list1[i] > dp[j] and list1[i] < dp[j+1]:
            dp.insert(j, list1[i])
            break
            
        elif max(dp) < list1[i]:
            dp.append(list1[i])
            break
print(dp)
for i in range(m):
    for j in range(0, len(dp)-1):
        
        if list2[i] == dp[j]:
            break

        if list2[i] > dp[j] and list2[i] < dp[j+1]:
            dp.insert(j, list2[i])
            break
            
        elif max(dp) < list2[i]:
            dp.append(list2[i])
            break

print(dp)
print(len(dp))